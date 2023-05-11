
import streamlit as st
from joblib import load
import pandas as pd

model = load('dtree.joblib')


st.title('Enter the details below to predict if the booking will be cancelled or not')

# st.title('Enter the details below to predict if the booking will be cancelled or not')


stays_weekend = st.number_input('No. of nights weekend')

stays_week = st.number_input('No. of nights week')

options_meal = ('BB','FB','HB','SC','Undefined')
meal = st.selectbox('Meal',options_meal)

options_market =  ('Direct', 'Corporate', 'Online TA', 'Offline TA/TO','Complementary', 'Groups', 'Undefined', 'Aviation')
market = st.selectbox('Market Segment',options_market)

options_distribution_channel =  ('Direct', 'Corporate', 'TA/TO', 'Undefined', 'GDS')
distribution_channel = st.selectbox('Distribution Channel', options_distribution_channel)


repeated_guest = st.number_input('Is a repeated guest')

previous_cancellations = st.number_input('No. of previous cancellations')

previous_bookings_not_canceled = st.number_input('No. of previous bookings not cancelled')

options_reserved_room_type =   ('C', 'A', 'D', 'E', 'G', 'F', 'H', 'L', 'P', 'B')
reserved_room_type = st.selectbox('Reserved room type',options_reserved_room_type)

options_assigned_room_type =  ('C', 'A', 'D', 'E', 'G', 'F', 'I', 'B', 'H', 'P', 'L', 'K')
assigned_room_type = st.selectbox('Assigned room type', options_assigned_room_type)

options_deposit_type =  ('No Deposit', 'Refundable', 'Non Refund')
deposit_type = st.selectbox('Deposit type', options_deposit_type)

days_in_waiting_list = st.number_input('No. of days_in_waiting_list')

options_customer_type =  ('Transient', 'Contract', 'Transient-Party', 'Group')
customer_type = st.selectbox('Customer type', options_customer_type)

adr = st.number_input('Average rate per day')

required_car_parking_spaces = st.number_input('No. of required car parking spaces')

total_of_special_requests = st.number_input('No. of special requests')

options_reservation_status = ('Check-Out', 'Canceled', 'No-Show')
reservation_status = st.selectbox('Reservation status',options_reservation_status)

reservation_status_date = st.date_input('Reservation status date')

arrival_date = st.date_input('Arrival date')

total_number_of_people = st.number_input('Total number of people')

total_stays = st.number_input('Total nights of stay')



input_data = {'hotel' : 0,
            'stays_in_weekend_nights' : stays_weekend,
             'stays_in_week_nights': stays_week,
             'meal': options_meal.index(meal),
             'market_segment': options_market.index(market),
             'distribution_channel': options_distribution_channel.index(distribution_channel),
             'is_repeated_guest':repeated_guest,
             'previous_cancellations': previous_cancellations,
             'previous_bookings_not_canceled':previous_bookings_not_canceled,
             'reserved_room_type': options_reserved_room_type.index(reserved_room_type),
             'assigned_room_type': options_assigned_room_type.index(assigned_room_type),
             'deposit_type' : options_deposit_type.index(deposit_type),
             'days_in_waiting_list': days_in_waiting_list,
             'customer_type': options_customer_type.index(customer_type),
             'adr': adr,
             'required_car_parking_spaces': required_car_parking_spaces,
             'total_of_special_requests' : total_of_special_requests,
             'reservation_status' : options_reservation_status.index(reservation_status),
             'reservation_status_date' : reservation_status_date,
             'arrival_date' : arrival_date,
             'total_number_of_people': total_number_of_people,
             'total_stays': total_stays}

input_data_df = pd.DataFrame(input_data,index=[0])

input_data_df['reservation_status_date'] = pd.to_datetime(input_data_df['reservation_status_date'])

input_data_df['arrival_date'] = pd.to_datetime(input_data_df['arrival_date'])

input_data_df['arrival_date'] = input_data_df['arrival_date'].values.astype('float64')

input_data_df['reservation_status_date'] = input_data_df['reservation_status_date'].values.astype('float64')

res = model.predict(input_data_df)

st.write('prediction',res)

if st.button('predict'):
    st.write('prediction',res)
    if(res[0] == 1):
        st.success('The booking will not be cancelled')
    elif(res[0] == 0):
     st.info('The booking will be cancelled')
