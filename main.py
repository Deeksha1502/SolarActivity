import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',
         unsafe_allow_html=True  )


st.markdown(
    """
 <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Solar Spectrum</title>
        <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.11/typed.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/waypoints/4.0.1/jquery.waypoints.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css"/>
    </head>
    """
    , unsafe_allow_html=True
)

st.markdown("""
            
             
            <div class="scroll-up-btn">
        <i class="fas fa-angle-up"></i>
    </div>
    <nav class="navbar">
        <div class="max-width">
            <div class="logo"><a href="#">Solar<span>Spectrum.</span></a></div>
            <ul class="menu">
                <li><a href="#home" class="menu-btn">HOME</a></li>
                <li><a href="#sunspot" class="menu-btn">SUNSPOTS</a></li>
                <li><a href="#services" class="menu-btn">SOLAR FLARES</a></li>
                <li><a href="#Sunspots" class="menu-btn">CMES</a></li>
               
               
            </ul>
            <div class="menu-btn">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    
    <section class="home" id="home">
        <div class="max-width">
            <div class="home-content">
                <div class="text-1">Select the type of</div>
                <div class="text-2">Solar activity</div>
                <div class="text-3"><span class="typing"></span></div>
                <!-- <a href="#">sunspots button</a> -->
            </div>
        </div>
    </section>
       
            """
 , unsafe_allow_html=True)
