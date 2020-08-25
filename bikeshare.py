import get_filters as gf
import load_data as ld
import statistics as st

def main():
    while True:
        city, month, day = gf.get_filters()
        df = ld.load_data(city, month, day)

        st.time_stats(df, month, day)
        st.station_stats(df)
        st.trip_duration_stats(df)
        st.user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
