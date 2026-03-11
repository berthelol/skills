# TikTok API Endpoints

Base path: `/v1/tiktok`

## Profile & User Data

### Get Profile
```
GET /v1/tiktok/profile?handle={username}
```
Returns public profile data: bio, follower/following counts, total likes, avatar, verified status.

### Audience Demographics
```
GET /v1/tiktok/user/demographics?handle={username}
```
Returns audience country breakdown. **Costs 26 credits.**

### Followers
```
GET /v1/tiktok/user/followers?handle={username}&cursor={cursor}
```
Paginated list of followers.

### Following
```
GET /v1/tiktok/user/following?handle={username}&cursor={cursor}
```
Paginated list of accounts the user follows.

## Video Content

### User Posts (Profile Videos)
```
GET /v1/tiktok/profile/videos?handle={username}&cursor={cursor}&sort_by={sort}
```
Paginated list of a user's videos. `sort_by=popular` returns most popular first.
Response contains `aweme_list` array with video objects. Each video has `statistics` with `play_count`, `digg_count` (likes), `comment_count`, `share_count`, `collect_count`.

### Video Info
```
GET /v1/tiktok/video?video_id={id}
```
Full details for a single video: description, play/like/comment/share counts, music info, hashtags.

### Video Transcript
```
GET /v1/tiktok/video/transcript?video_id={id}
```
Returns the transcript of a TikTok video. Note: AI-generated transcripts are limited to videos under 2 minutes.

### Video Comments
```
GET /v1/tiktok/video/comments?video_id={id}&cursor={cursor}
```
Paginated comments on a video.

### Live Stream
```
GET /v1/tiktok/user/live?handle={username}
```
Data from a user's current or recent live stream.

## Search

### Search by Keyword
```
GET /v1/tiktok/search?query={keyword}&cursor={cursor}
```
Search TikTok videos matching a keyword.

### Top Search
```
GET /v1/tiktok/search/top?query={keyword}
```
Returns the "Top" search results including photo carousels and videos (regular keyword search only returns videos).

### Search by Hashtag
```
GET /v1/tiktok/search/hashtag?query={hashtag}&cursor={cursor}
```
Videos tagged with a specific hashtag.

### Search Users
```
GET /v1/tiktok/search/users?query={keyword}&cursor={cursor}
```
Search for TikTok users.

## Trending & Discovery

### Popular Videos
```
GET /v1/tiktok/videos/popular?period={period}&region={region}
```
Filter trending videos by time period and region.

### Popular Creators
```
GET /v1/tiktok/creators/popular?min_followers={count}&audience_country={country}
```
Discover creators by follower count, audience country, and engagement.

### Popular Hashtags
```
GET /v1/tiktok/hashtags/popular?period={period}
```
Trending hashtags with time-period filtering.

### Popular Songs
```
GET /v1/tiktok/songs/popular
```
Trending music on TikTok (30-second previews max).

### Trending Feed
```
GET /v1/tiktok/trending
```
The trending feed from TikTok.

## Music

### Song Details
```
GET /v1/tiktok/song?song_id={id}
```
Metadata for a specific song.

### TikToks Using Song
```
GET /v1/tiktok/song/videos?song_id={id}&cursor={cursor}
```
Videos that use a specific song.

## TikTok Shop

### Shop Search
```
GET /v1/tiktok/shop/search?query={keyword}
```
Search TikTok Shop products.

### Product Details
```
GET /v1/tiktok/product?product_id={id}
```
Full product details including exact stock count, related promotional videos.

### Product Reviews
```
GET /v1/tiktok/product/reviews?product_id={id}
```
Returns up to 100 product reviews at once.

## Common parameters

- `trim=true` — trimmed response with key fields only
- `cursor` — pagination cursor from previous response
- `sort_by=popular` — sort user posts by popularity
