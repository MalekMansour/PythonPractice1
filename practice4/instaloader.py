import instaloader

bot = instaloader.Instaloader()

username = input("Enter the user name: ")
profile = instaloader.Profile.from_username(bot.context, username)

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)