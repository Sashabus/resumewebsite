from pandas import DataFrame, concat
from plotly.express import choropleth, pie, bar, colors
from pycountry_convert import country_mappings


class Time:
    separate_time_df = DataFrame([], columns=["day", "hour"])  # df of separated day and hour

    @classmethod
    def fill_separate_time_df(cls, time):
        """
        This method takes variable time that must be in time format(2022-06-20 22:48:22) divides this value into
        different categories(day, hour) and appends them separately to the `sep_time_df` DataFrame.
        param time: takes value of time from the main DataFrame
        """
        time = time.split()
        sep_time_new_el_df = DataFrame([[time[0], int(time[1].split(':')[0])]], columns=["day", "hour"])
        cls.separate_time_df = concat([cls.separate_time_df, sep_time_new_el_df], ignore_index=True)

    @classmethod
    def generate_average_time_df(cls):
        """
        takes data out of sep_time_df df and based on data generates df of frequency of different hours.
        return: returns the value of generated dataframe
        """
        average_time_df = DataFrame(columns=['average number of entrances per day'])  # new empty df is created
        average_time_df.index.name = 'hour'  # just to make df and graph more clear
        rows = len(cls.separate_time_df.copy().groupby('day')['day'])  # rows - number of unique days in the data
        for i in range(24):
            """
            finds average number of entrances on website for every hour in day per every day
            """
            average_time_df.loc[f'hour {i}-{i + 1}'] = [
                round(cls.separate_time_df['hour'].value_counts()[i] / rows, 1)]
        return average_time_df

    @classmethod
    def get_aver_graph(cls, dataframe):
        dataframe['created'].copy().dropna().astype("string").apply(cls.fill_separate_time_df)
        return bar(data_frame=cls.generate_average_time_df(), y='average number of entrances per day')
        # title='average number of entrances on the website every hour in a day per day'


def get_advertisement_graph(dataframe):
    ad_stats = dataframe[['so', 'unique']].dropna().groupby('so').sum()
    return pie(data_frame=ad_stats, values='unique', names=ad_stats.index,
               title='percent of people who came from different ad resources')


class Country:
    @staticmethod
    def country_alpha2_to_country_alpha3(country_2_code, ignore_non_elements=True):
        """Convert country ISO 3166-1 Alpha-2 code to country ISO 3166-1 Alpha-3.
        """
        if country_2_code is None or len(country_2_code) != 2:
            if ignore_non_elements:
                return None
            raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

        dict_country_alpha2_to_country_alpha3 = country_mappings.map_country_alpha2_to_country_alpha3()

        if country_2_code not in dict_country_alpha2_to_country_alpha3:
            if ignore_non_elements:
                return None
            raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

        return dict_country_alpha2_to_country_alpha3[country_2_code]

    @classmethod
    def get_country_graph(cls, dataframe):
        country_stats = dataframe[['cc', 'unique']].dropna()
        country_stats['cc'] = country_stats['cc'].apply(cls.country_alpha2_to_country_alpha3).dropna()
        country_stats = country_stats.groupby('cc').sum()
        return choropleth(country_stats, locations=country_stats.index, color='unique',
                          hover_name=country_stats.index,
                          color_continuous_scale=colors.sequential.Plasma)
