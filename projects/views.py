from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Project
from django.contrib import messages

User = get_user_model()

@login_required
def project_list(request):
    user = request.user
    if user.role == 'admin':
        projects = Project.objects.filter(owner=user)
    else:
        projects = Project.objects.filter(members=user)
    
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Check access
    if not (request.user == project.owner or request.user in project.members.all()):
        messages.error(request, "Access denied.")
        return redirect('project_list')
        
    all_users = User.objects.exclude(id__in=project.members.all())
    return render(request, 'projects/project_detail.html', {'project': project, 'all_users': all_users})

@login_required
def add_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.owner:
        messages.error(request, "Only project owners can add members.")
        return redirect('project_detail', pk=pk)
        
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_to_add = get_object_or_404(User, id=user_id)
        project.members.add(user_to_add)
        messages.success(request, f"{user_to_add.username} added to project.")
        
    return redirect('project_detail', pk=pk)


@login_required
def project_create(request):
    if request.user.role != 'admin':
        messages.error(request, "Only admins can create projects.")
        return redirect('project_list')
        
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        project = Project.objects.create(name=name, description=description, owner=request.user)
        # Add creator as member by default
        project.members.add(request.user)
        messages.success(request, "Project created successfully.")
        return redirect('project_list')
    
    return render(request, 'projects/project_form.html')
