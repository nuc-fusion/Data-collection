purpose_system = """I want you to act as a Website Reader. Your objective is to explain a website's purpose and usage, given the website's text. Your explanation should cover all of the website's primary functions. DONOT GUESS the purpose of the website, you SHOULD output \"None\" If you are not PRETTY sure about the purpose of the website. Note that you should only answer the purpose or usage within 20 words."""

example_in = """
    Apple

  - Apple
  -     - Store

    - Mac

    - iPad

    - iPhone

    - Watch

    - Vision

    - AirPods

    - TV & Home

    - Entertainment

    - Accessories

    - Support

Shop and Learn Shop and Learn +

  - Store
  - Mac
  - iPad
  - iPhone
  - Watch
  - Vision
  - AirPods
  - TV & Home
  - AirTag
  - Accessories
  - Gift Cards

Apple Wallet Apple Wallet +

  - Wallet
  - Apple Card
  - Apple Pay
  - Apple Cash

Account Account +

  - Manage Your Apple ID
  - Apple Store Account
  - iCloud.com

Entertainment Entertainment +

  - Apple One
  - Apple TV+
  - Apple Music
  - Apple Arcade
  - Apple Fitness+
  - Apple News+
  - Apple Podcasts
  - Apple Books
  - App Store

Apple Store Apple Store +

  - Find a Store
  - Genius Bar
  - Today at Apple
  - Apple Camp
  - Apple Store App
  - Certified Refurbished
  - Apple Trade In
  - Financing
  - Carrier Deals at Apple
  - Order Status
  - Shopping Help

For Business For Business +

  - Apple and Business
  - Shop for Business

For Education For Education +

  - Apple and Education
  - Shop for K-12
  - Shop for College

For Healthcare For Healthcare +

  - Apple in Healthcare
  - Health on Apple Watch
  - Health Records on iPhone

For Government For Government +

  - Shop for Government
  - Shop for Veterans and Military

Apple Values Apple Values +

  - Accessibility
  - Education
  - Environment
  - Inclusion and Diversity
  - Privacy
  - Racial Equity and Justice
  - Supplier Responsibility

About Apple About Apple +

  - Newsroom
  - Apple Leadership
  - Career Opportunities
  - Investors
  - Ethics & Compliance
  - Events
  - Contact Apple

More ways to shop: Find an Apple Store or other retailer near you. Or call 1-800-MY-APPLE.
"""

example_out = """
    The purpose of the website is to showcase and sell a variety of Apple products and accessories, serving as a platform for users to explore, learn about, and purchase Apple products and services..
"""

purpose_query = '#Website Text#:\n%s\n\n#Purpose#:\n'

no_purpose = 'None'