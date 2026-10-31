"""Original practice problem sets for Coordinates and Times.

The five Basic Astrophysics PDFs use past-paper identifiers instead of
newly generated exercises.
"""
SETS = {
    '02.01': [
        ('Altitude at culmination', 'An observer at latitude 48° N observes a star of declination +20°. Assume a spherical Earth and ignore refraction. (a) Find the star’s altitude at upper culmination using h = 90° − |latitude − declination|. (b) Is the star north or south of the zenith at upper culmination? (c) Explain why its hour angle is zero at that instant.'),
        ('Circumpolar skies', 'An observer is at 48° N. Ignore atmospheric refraction and local obstructions. (a) Find the minimum declination for a star to remain above the horizon throughout its daily motion, allowing the limiting case to touch the horizon. (b) Determine whether stars at declinations +50° and +30° are circumpolar. (c) Which declinations never rise above the horizon?'),
        ('Right ascension and hour angle', 'The local sidereal time is 10 h 20 min. A star has right ascension 8 h 50 min. (a) Find its hour angle using H = LST − RA. (b) Is it east or west of the local meridian? (c) How long ago did it cross the meridian, in sidereal time? State your sign convention.'),
        ('Seasons on the celestial sphere', 'The Earth’s rotation axis is tilted relative to the normal to its orbital plane. (a) Describe the celestial equator and the ecliptic. (b) Why does the Sun’s declination change during the year? (c) Explain the meaning of an equinox and a solstice. Do not assume the Earth–Sun distance causes the seasons.'),
    ],
    '02.02': [
        ('Solar and sidereal days', 'A mean solar day is 24 h and a sidereal day is approximately 23 h 56 min 4 s. (a) Explain why the sidereal day is shorter in terms of Earth’s orbit. (b) A star transits at 22:00 mean solar time tonight. Estimate its transit time 30 days later, ignoring small variations. (c) Explain why the result is approximate.'),
        ('Longitude and local time', 'Two observers are at longitudes 105° E and 75° E. Ignore the equation of time. (a) Find the difference between their local mean solar times. (b) If it is 12:00 local mean solar time at 105° E, what is it at 75° E? (c) Explain why civil time zones need not agree exactly with local mean solar time.'),
        ('Julian dates', 'Julian dates change continuously in days, and JD 2451545.0 corresponds to 2000 January 1 at 12:00 UT. (a) What is the JD at 18:00 UT on the same date? (b) What is the JD at 00:00 UT on January 2? (c) If an event at JD 2451545.25 lasts 90 minutes, find the JD at its end. Ignore leap seconds.'),
        ('Different years and timing corrections', 'A sidereal year measures Earth’s orbital period relative to distant stars; a tropical year measures the cycle of seasons. (a) Explain why these definitions differ because of precession. (b) Define the equation of time as apparent solar time minus mean solar time, and explain qualitatively why it varies through the year. (c) Why can a heliocentric Julian date be useful when comparing observations of a periodic astronomical event taken months apart?'),
    ],
}
