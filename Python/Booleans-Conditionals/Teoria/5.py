print(True or True and False)

prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

prepared_for_weather = have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)

prepared_for_weather = have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))

prepared_for_weather = (
    have_umbrella 
    or ((rain_level < 5) and have_hood) 
    or (not (rain_level > 0 and is_workday))
)
