from albums.models import Album
albums = Album.objects.all()
for a in albums:
    print(f'Album: {a.title} | Passkey: "{a.passkey}"')
