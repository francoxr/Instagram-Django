"""Posts views."""

# Django
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models 
from posts.models import Post

#Forms
from posts.forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'

# @login_required
# def list_posts(request):
#     """List existing posts"""
#     posts = Post.objects.all().order_by('-created')

#     return render(request, 'posts/feed.html', {'posts': posts})


class PostView(LoginRequiredMixin, DetailView):
    """Return one published post."""

    template_name = 'posts/detail.html'
    model = Post
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'post' 


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


# @login_required
# def create_post(request):
#     """Create post view"""
#     if request.method == "POST" :
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile,
#         }
#     )