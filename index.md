<style>
  .container {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
  }
  .image-container {
    flex: 40%;
    padding-right: 20px;
    text-align: center;
  }
  .image-container img {
    width: 100%;
    border-radius: 10px;
  }
  .caption {
    font-size: 0.8em;
    color: gray;
    margin-top: 5px;
    text-align: center;
  }
  .text-container {
    flex: 60%;
  }

  /* Mobile: Stack image, caption, and text */
  @media (max-width: 768px) {
    .container {
      flex-direction: column;
    }
    .image-container {
      padding-right: 0;
    }
  }
</style>

<div class="container">
  <div class="image-container">
    <img src="assets/sayam.JPG" alt="My Photo">
    <p class="caption">This is me patiently waiting outside a restaurant to have food.</p>
  </div>
  <div class="text-container">
    <p>
    
Hello all and welcome to my blog. I am Sayam Kumar, an AI Research Engineer @ <a href="https://phaidra.ai">Phaidra</a> where we create AI-powered control systems for industrial processes.<br><br>

I love to work in the field of AI because I am inspired by observing how AI positively impacts various domains like healthcare, astronomy, climate-change, e-commerce, etc.<br><br>

In my free time, I like to travel, play chess and listen to Punjabi/Hindi music.<br><br>

This year I am looking forward to dig deeper into intersection of Reinforcement Learning and Bayesian statistics, improve my fitness consistently, and pick up learning violin.<br><br>
    </p>
  </div>
</div>
