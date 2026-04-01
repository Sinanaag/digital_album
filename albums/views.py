from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Photo


# ─── ALBUM VIEWS ──────────────────────────────────────────────────────────────

def home(request):
    # Everyone can see the list of albums — no login needed
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums': albums})


def enter_passkey(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    error = False

    if request.method == 'POST':
        entered_key = request.POST.get('passkey', '')  # Get what user typed

        if entered_key == album.passkey:
            # ✅ Correct! Remember unlock in the session
            request.session[f'album_{album_id}_unlocked'] = True
            return redirect('album_detail', album_id=album_id)
        else:
            # ❌ Wrong passkey
            error = True

    return render(request, 'album_passkey.html', {'album': album, 'error': error})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    # If this album has a passkey, check if user has unlocked it
    if album.passkey:
        unlocked = request.session.get(f'album_{album_id}_unlocked', False)
        if not unlocked:
            return redirect('enter_passkey', album_id=album_id)

    # No passkey OR already unlocked → show photos
    photos = Photo.objects.filter(album=album)
    return render(request, 'album_detail.html', {'album': album, 'photos': photos})
