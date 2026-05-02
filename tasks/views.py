from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from projects.models import Project
from tasks.models import Task
from django.db.models import Count, Q

@login_required
def dashboard(request):
    """
    Main dashboard view. Shows stats based on user role.
    Admins see everything they own, Members see what they are assigned to.
    """
    user = request.user
    if user.role == 'admin':
        projects = Project.objects.filter(owner=user)
        tasks = Task.objects.filter(project__owner=user)
    else:
        projects = Project.objects.filter(members=user)
        tasks = Task.objects.filter(assignee=user)


    stats = {
        'total_tasks': tasks.count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'done': tasks.filter(status='done').count(),
        'overdue': tasks.filter(due_date__lt=timezone.now()).exclude(status='done').count(),
    }

    context = {
        'projects': projects,
        'recent_tasks': tasks.order_by('-created_at')[:5],
        'stats': stats,
    }
    return render(request, 'dashboard.html', context)

@login_required
def task_list(request):
    user = request.user
    if user.role == 'admin':
        tasks = Task.objects.filter(project__owner=user)
    else:
        tasks = Task.objects.filter(assignee=user)
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # Only assignee or project owner can update status
    if not (request.user == task.assignee or request.user == task.project.owner):
        messages.error(request, "Permission denied.")
        return redirect('task_list')
        
    if request.method == 'POST':
        new_status = request.POST.get('status')
        new_progress = request.POST.get('progress')
        
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            # Auto-set progress to 100 if Done
            if new_status == 'done':
                task.progress = 100
        
        if new_progress is not None:
            try:
                prog = int(new_progress)
                task.progress = max(0, min(100, prog))
                # Auto-set status to In Progress if progress > 0
                if task.progress > 0 and task.progress < 100:
                    task.status = 'in_progress'
                elif task.progress == 100:
                    task.status = 'done'
            except ValueError:
                pass
                
        task.save()
        messages.success(request, f"Task '{task.title}' updated.")

            
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))

@login_required
def task_create(request):
    if request.user.role != 'admin':
        messages.error(request, "Only admins can create tasks.")
        return redirect('task_list')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        project_id = request.POST.get('project')
        assignee_id = request.POST.get('assignee')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        
        project = Project.objects.get(id=project_id, owner=request.user)
        task = Task.objects.create(
            title=title, 
            description=description, 
            project=project,
            assignee_id=assignee_id if assignee_id else None,
            due_date=due_date if due_date else None,
            priority=priority
        )
        messages.success(request, "Task created successfully.")
        return redirect('task_list')

    user = request.user
    projects = Project.objects.filter(owner=user)
    from django.contrib.auth import get_user_model
    User = get_user_model()
    users = User.objects.all()
    
    return render(request, 'tasks/task_form.html', {'projects': projects, 'users': users})
