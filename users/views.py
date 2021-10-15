"""Users views."""

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user' 

    def get_context_data(self, **kwargs):
        """Add user's post to context."""
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(profile_id=user.profile.id).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile View."""

    template_name = 'users/update.html'
    model = Profile
    form_class = ProfileForm
    # fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""

        return self.request.user.profile
    
    def get_success_url(self):
        """Return to user's profile"""

        username = self.object.user.username
        print(self)
        return reverse('users:detail', kwargs={'username': username})

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        print(self)
        return context

# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
            
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()


#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)

#     else:
#         form = ProfileForm()

#     context = {
#         "profile": profile,
#         "user": request.user,
#         "form": form,
#     }
#     return render(request,'users/update.html',context=context)

class LoginView(auth_views.LoginView):
    """Login View"""

    template_name = 'users/login.html'

# def login_view(request):
#     """Login view"""

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(request,username=username,password=password)

#         if user:
#             login(request,user)
#             return redirect('posts:feed')
#         else:
#             data = {
#                 'error':'invalid username and password'
#             }
#             return render(request, 'users/login.html', {'data': data})

#     return render(request,'users/login.html')


@login_required
def logout_view(request):
    """Logout view"""
    print('aqui')
    logout(request)
    return redirect('users:login')


class SignUpView(FormView):
    """User Signup view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        
        form.save()
        return super().form_valid(form)



# def signup_view(request):
#     """Signup view"""

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )