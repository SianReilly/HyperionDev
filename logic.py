# ========= Task 1.3 ===========
# This Logical Error prints the solar system object you expect to see at a certain time in the sky.
# The Logical Error is that the moon is assumed here as always visible at daytime.
# This is not true as the moon is not always visible in daytime as the sky is usually too bright.

def print_sky_object(time_of_day):
    if time_of_day == 'daytime':
        sky_object = 'moon'
    else:
        sky_object ='stars'
    print(f"During the {time_of_day}, you can always see the {sky_object} in the sky.")


# Thus calling the function will return the wrong logical answer = moon in day.

print_sky_object('daytime')