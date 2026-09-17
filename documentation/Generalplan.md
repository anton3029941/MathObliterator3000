## Requirements
### The goal
A web application that receives a photo, accurately transcribes mathematical formulas into LaTeX code, and sends back a solution.

### Data Flow
HTML form accepts an image and sends it to the server. Then the server analyses it, calculates and returns a solution.

### Infrastructure
/MathObliterator3000
    /server
        /server.py <- entry
        /transcribe.py
        /solve.py
    /website
        /home.html
        /style.css

### Stack


### Consider
DDoS/DoS attacks, image resolution/file size, invalid file extensions