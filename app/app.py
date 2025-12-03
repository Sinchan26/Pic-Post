from fastapi import FastAPI,HTTPException
app=FastAPI()

text_posts={1:{"title":"First Post","content":"This is the content of the first post."},
            2:{"title":"Second Post","content":"This is the content of the second post."}}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit and limit<=len(text_posts):
        return {key:text_posts[key] for key in list(text_posts)[:limit]}
    return text_posts
@app.get("/posts/{post_id}")
def get_post(post_id:int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(post_id)