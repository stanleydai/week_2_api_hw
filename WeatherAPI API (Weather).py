#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[155]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[156]:


url_weather = "http://api.weatherapi.com/v1/current.json?key=c43d6948ce4a493f93504326221406&q=70005&aqi=no"

response = requests.get(url_weather)

weather_data = response.json()


# In[157]:


print(weather_data['location']['tz_id'])


# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[158]:


print(weather_data['current']['wind_mph'], "mph")


# In[159]:


print(round(weather_data['current']['feelslike_f']-weather_data['current']['temp_f']), "degrees")


# In[ ]:





# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[160]:


url_moon = "http://api.weatherapi.com/v1/astronomy.json?key=c43d6948ce4a493f93504326221406&q=Metairie&dt=2022-06-17"

response = requests.get(url_moon)

moon_data = response.json()


# In[161]:


print("A", moon_data['astronomy']['astro']['moon_phase'], "will be visible!")


# In[ ]:





# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[162]:


url_weather = "http://api.weatherapi.com/v1/forecast.json?key=c43d6948ce4a493f93504326221406&q=Metairie&days=3&aqi=no&alerts=no"

response = requests.get(url_weather)

weather_data = response.json()


# In[163]:


print(round(weather_data['forecast']['forecastday'][0]['day']['maxtemp_f'] - weather_data['forecast']['forecastday'][0]['day']['mintemp_f']), "degrees")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[164]:


#the url variable and the name of the data dictionary - I'd  name them "_[whatever]". 


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[165]:


for x in weather_data['forecast']['forecastday']:
    print(x['day']['maxtemp_f'])
    if x['day']['maxtemp_f'] > 85: 
        print("it's really freakin hot.")
    else:
        print("it's not really freakin hot, but it's still Louisiana in June.")
    


# In[ ]:





# In[ ]:





# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[166]:


#the free plan only lets you go 3 days into the future, not more


# In[ ]:





# In[ ]:





# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[ ]:





# In[167]:


hotest = 0

for x in weather_data['forecast']['forecastday']:
    if (x['day']['maxtemp_f']) > hotest:
        hotest = (x['day']['maxtemp_f'])
    if hotest == (x['day']['maxtemp_f']): 
        print(x['date'])
        print(hotest)




# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[168]:


url_miami = "http://api.weatherapi.com/v1/forecast.json?key=c43d6948ce4a493f93504326221406&q=Miami&days=1&aqi=no&alerts=no"

response = requests.get(url_miami)

miami_data = response.json()


# In[169]:


for x in miami_data['forecast']['forecastday']:
    for y in x['hour']:
        if y['cloud']> 50:
            print(y['temp_f'], 'and','cloudy' )
        else:
            print(y['temp_f'])


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[170]:


count=0

for x in miami_data['forecast']['forecastday']:
    for y in x['hour']:
            print(y['temp_f'])
            if y['temp_f'] > 85:
                count = count + 1 
            
print("The percent of the time the temperature is above 85 is", round(count/24*100), "%.")


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[171]:


#At least 4 dollar a month!


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[172]:


#I could reach out, I could share passwords, I could ask the institution I'm working for.... could I create two accounts and have two api keys??


# In[ ]:





# In[ ]:




