class SpaceAge:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def calc_years(self, period: float) -> float:
        return round(self.seconds / (31557600 * period), 2)

    def on_earth(self) -> float:
        return self.calc_years(1)

    def on_mercury(self) -> float:
        return self.calc_years(0.2408467)

    def on_venus(self) -> float:
        return self.calc_years(0.61519726)

    def on_mars(self) -> float:
        return self.calc_years(1.8808158)

    def on_jupiter(self) -> float:
        return self.calc_years(11.862615)

    def on_saturn(self) -> float:
        return self.calc_years(29.447498)

    def on_uranus(self) -> float:
        return self.calc_years(84.016846)

    def on_neptune(self) -> float:
        return self.calc_years(164.79132)