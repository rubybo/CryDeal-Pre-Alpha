from django.shortcuts import render, redirect


# Redirecting user to login or redirecting to main
def main(request):
    if not request.user.is_authenticated:
        return redirect('loginning:user-login')
    return render(request, 'core/base.html')
