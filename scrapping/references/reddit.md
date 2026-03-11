# Reddit API Endpoints

Base path: `/v1/reddit`

## Profiles

### User Profile
```
GET /v1/reddit/profile?handle={username}
```
Public Reddit user profile data.

## Subreddits

### Subreddit Details
```
GET /v1/reddit/subreddit?name={subreddit_name}
```
Details about a subreddit. Also accepts a URL.

### Subreddit Posts
```
GET /v1/reddit/subreddit/posts?name={subreddit_name}&cursor={cursor}
```
Recent posts from a subreddit with engagement metrics.

### Subreddit Search
```
GET /v1/reddit/subreddit/search?name={subreddit_name}&query={keyword}&cursor={cursor}
```
Search within a subreddit for posts, comments, or media matching a query.

## Posts & Comments

### Post Comments
```
GET /v1/reddit/post/comments?url={post_url}&cursor={cursor}
```
Comments and post information from a Reddit post.

## Search

### Search Reddit
```
GET /v1/reddit/search?query={keyword}&cursor={cursor}
```
Search Reddit for posts across all subreddits.

## Ad Library

### Search Ads
```
GET /v1/reddit/ads/search?query={keyword}
```
Search the Reddit Ad Library. **Max 30 ads returned.**

### Get Ad
```
GET /v1/reddit/ad?ad_id={id}
```
Details for a specific Reddit ad by ID.

## Notes

- Subreddit details accepts both a name and a full URL
- Reddit ad search is capped at 30 results
- Use `trim=true` to reduce response size
- Use `cursor` for pagination on all paginated endpoints
