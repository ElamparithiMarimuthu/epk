from flask import Flask, render_template

app = Flask(__name__)

# Your microservices classes and logic go here (from the previous Python code)

# Sample route to render the HTML template
@app.route('/')
def index():
    # Use microservices to get data
    love_score = love_microservice.calculate_love_score()
    affection_level = affection_microservice.calculate_affection_level()
    one_sided_love = onesided_love_microservice.check_one_sided_love()
    age_compatible = age_microservice.check_age_compatibility()

    return render_template('index.html', 
                           boy_name=boy_name,
                           girl_name=girl_name,
                           love_score=love_score,
                           affection_level=affection_level,
                           one_sided_love=one_sided_love,
                           age_compatible=age_compatible)

if __name__ == '__main__':
    app.run(debug=True)
