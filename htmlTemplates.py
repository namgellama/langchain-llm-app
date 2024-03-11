css = """
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}

.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  height: 78px; 
    width: 78px; 
    border-radius: 50%; 
    object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
"""


bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://pbs.twimg.com/profile_images/1232518700/Endhiran-Movie-Wallpapers-6_1__400x400.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""


user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.giantfreakinrobot.com/wp-content/uploads/2022/08/bryan-cranston.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
