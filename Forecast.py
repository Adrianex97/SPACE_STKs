# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:03:37 2025

@author: 39366
"""

mport subprocess
tickers = ['TSLA','BA','LMT','NOC','RTX','SPCE','KTOS','LDOS','RKLB','LUNR','RDW']
raw = yf.download(tickers, period='1y', interval='1d', group_by='ticker', auto_adjust=True)

data = pd.DataFrame({t: raw[t]['Close'] for t in tickers}).dropna()

# Loop su ogni ticker
for ticker in tickers:
    print(f"=== Elaborazione {ticker} ===")
    df = data[[ticker]].reset_index().rename(columns={'Date':'ds', ticker:'y'})
    m = Prophet(daily_seasonality=True, yearly_seasonality=True)
    m.fit(df)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)

    # Grafico interattivo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Storico'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
    fig.add_trace(go.Scatter(
        x=forecast['ds'], y=forecast['yhat_upper'],
        fill='tonexty', mode='lines', name='Upper CI', line=dict(width=0),
        fillcolor='rgba(255,165,0,0.2)'
    ))
    fig.add_trace(go.Scatter(
        x=forecast['ds'], y=forecast['yhat_lower'],
        fill='tonexty', mode='lines', name='Lower CI', line=dict(width=0),
        fillcolor='rgba(255,165,0,0.2)'
    ))
    fig.update_layout(
        title=f'Forecast 1 anno per {ticker} con Prophet',
        xaxis_title='Data', yaxis_title='Prezzo ($)',
        template='plotly_dark'
    )
    # Se preferisci salvare in HTML:
    # fig.write_html(f"{ticker}_forecast.html")
    fig.show()

    # Componenti trend/stagionalità
    comp = m.plot_components(forecast)
    comp.suptitle(f"Componenti di {ticker}", y=0.9)