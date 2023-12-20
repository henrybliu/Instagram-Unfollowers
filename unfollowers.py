from following import *
from followers import *

#parse followingString
followingParse = followingString.split('\n')
followingUserParse = []
followingParse = followingParse[1::]
followingParse = followingParse[:len(followingParse)-1:]
followingParse = followingParse[::2]
following = set(followingParse)
print(len(following))

#parse followersString
followersParse = followersString.split('\n')
followersUserParse = []
followersParse = followersParse[1::]
followersParse = followersParse[:len(followersParse)-1:]
followersParse = followersParse[::2]
followers = set(followersParse)
print(len(followers))

#print unfollowers
unfollowers = []
for user in following:
    if user not in followers:
        unfollowers.append(user)
print(unfollowers)