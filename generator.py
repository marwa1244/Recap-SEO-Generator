import random

def generate_recap_metadata(movie_name):
    # Psychological title templates for high CTR
    templates = [
        f"Why Everyone Is Talking About {movie_name} - Ending Explained",
        f"He Thought He Was Safe, But... | {movie_name} Recap",
        f"10 Things You Missed in {movie_name}",
        f"The Most Disturbing Scenes in {movie_name} Revealed",
        f"Don't Watch {movie_name} Until You See This!"
    ]
    
    # Recommended SEO Tags
    seo_tags = f"movie recap, film summary, {movie_name} review, {movie_name} explained, cinema, trending movies"
    
    # AI Image Prompt for Thumbnails (Octane Render Style)
    thumbnail_prompt = f"Cinematic 8k photo of a key scene from {movie_name}, hyper-realistic, octane render, 70mm lens, dramatic lighting, detailed textures."

    print(f"--- Metadata for: {movie_name} ---")
    print(f"Suggested Title: {random.choice(templates)}")
    print(f"SEO Tags: {seo_tags}")
    print(f"Thumbnail AI Prompt: {thumbnail_prompt}")

# Example Usage
if __name__ == "__main__":
    movie = input("Enter the movie name: ")
    generate_recap_metadata(movie)

