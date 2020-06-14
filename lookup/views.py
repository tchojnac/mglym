from django.shortcuts import render


# http://api.gios.gov.pl/pjp-api/rest/station/findAll

def home(request):
    import json
    import requests

    if request.method == 'POST':
        #stationId = request.POST['stationId']
        stationId = {'Wrocław': 117,
                    'Warszawa': 550,
                    'Gdańsk': 729
                    }


        api_request = requests.get(
              'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        if api['stIndexLevel']['indexLevelName'] == 'Bardzo dobry':
            category_description = 'Jakość powietrza jest bardzo dobra, zanieczyszczenie powietrza nie stanowi zagrożenia dla zdrowia, warunki bardzo sprzyjające do wszelkich aktywności na wolnym powietrzu, bez ograniczeń.'
            category_color = 'good'

        elif api['stIndexLevel']['indexLevelName'] == 'Dobry':
            category_description = 'Jakość powietrza jest zadowalająca, zanieczyszczenie powietrza powoduje brak lub niskie ryzyko zagrożenia dla zdrowia. Można przebywać na wolnym powietrzu i wykonywać dowolną aktywność, bez ograniczeń.'
            category_color = 'moderate'

        elif api['stIndexLevel']['indexLevelName'] == 'Umiarkowany':
            category_description = 'Jakość powietrza jest akceptowalna. Zanieczyszczenie powietrza może stanowić zagrożenie dla zdrowia w szczególnych przypadkach (dla osób chorych, osób starszych, kobiet w ciąży oraz małych dzieci). Warunki umiarkowane do aktywności na wolnym powietrzu.'
            category_color = 'usg'
        elif api['stIndexLevel']['indexLevelName'] == 'Dostateczny':
            category_description = 'Jakość powietrza jest dostateczna, zanieczyszczenie powietrza stanowi zagrożenie dla zdrowia (szczególnie dla osób chorych, starszych, kobiet w ciąży oraz małych dzieci) oraz może mieć negatywne skutki zdrowotne. Należy rozważyć ograniczenie (skrócenie lub rozłożenie w czasie) aktywności na wolnym powietrzu, szczególnie jeśli ta aktywność wymaga długotrwałego lub wzmożonego wysiłku fizycznego.'
            category_color = 'Unhealthy'
        elif api['stIndexLevel']['indexLevelName'] == 'Zły':
            category_description = 'Jakość powietrza jest zła, osoby chore, starsze, kobiety w ciąży oraz małe dzieci powinny unikać przebywania na wolnym powietrzu. Pozostała populacja powinna ograniczyć do minimum wszelką aktywność fizyczną na wolnym powietrzu - szczególnie wymagającą długotrwałego lub wzmożonego wysiłku fizycznego.'
            category_color = 'veryunhealthy'
        elif api['stIndexLevel']['indexLevelName'] == 'Bardzo zły':
            category_description = 'Jakość powietrza jest bardzo zła i ma negatywny wpływ na zdrowie. Osoby chore, starsze, kobiety w ciąży oraz małe dzieci powinny bezwzględnie unikać przebywania na wolnym powietrzu. Pozostała populacja powinna ograniczyć przebywanie na wolnym powietrzu do niezbędnego minimum. Wszelkie aktywności fizyczne na zewnątrz są odradzane. Długotrwała ekspozycja na działanie substancji znajdujących się w powietrzu zwiększa ryzyko wystąpienia zmian m.in. w układzie oddechowym, naczyniowo-sercowym oraz odpornościowym.'
            category_color = 'hazardous'

        return render(request, 'home.html',
                      {'api': api, 'stIndexLevel': category_description, 'category_color': category_color})

    else:

        api_request = requests.get(
            'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/944')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        if api['stIndexLevel']['indexLevelName'] == 'Bardzo dobry':
            category_description = 'Jakość powietrza jest bardzo dobra, zanieczyszczenie powietrza nie stanowi zagrożenia dla zdrowia, warunki bardzo sprzyjające do wszelkich aktywności na wolnym powietrzu, bez ograniczeń.'
            category_color = 'good'

        elif api['stIndexLevel']['indexLevelName'] == 'Dobry':
            category_description = 'Jakość powietrza jest zadowalająca, zanieczyszczenie powietrza powoduje brak lub niskie ryzyko zagrożenia dla zdrowia. Można przebywać na wolnym powietrzu i wykonywać dowolną aktywność, bez ograniczeń.'
            category_color = 'moderate'

        elif api['stIndexLevel']['indexLevelName'] == 'Umiarkowany':
            category_description = 'Jakość powietrza jest akceptowalna. Zanieczyszczenie powietrza może stanowić zagrożenie dla zdrowia w szczególnych przypadkach (dla osób chorych, osób starszych, kobiet w ciąży oraz małych dzieci). Warunki umiarkowane do aktywności na wolnym powietrzu.'
            category_color = 'usg'

        elif api['stIndexLevel']['indexLevelName'] == 'Dostateczny':
            category_description = 'Jakość powietrza jest dostateczna, zanieczyszczenie powietrza stanowi zagrożenie dla zdrowia (szczególnie dla osób chorych, starszych, kobiet w ciąży oraz małych dzieci) oraz może mieć negatywne skutki zdrowotne. Należy rozważyć ograniczenie (skrócenie lub rozłożenie w czasie) aktywności na wolnym powietrzu, szczególnie jeśli ta aktywność wymaga długotrwałego lub wzmożonego wysiłku fizycznego.'
            category_color = 'Unhealthy'

        elif api['stIndexLevel']['indexLevelName'] == 'Zły':
            category_description = 'Jakość powietrza jest zła, osoby chore, starsze, kobiety w ciąży oraz małe dzieci powinny unikać przebywania na wolnym powietrzu. Pozostała populacja powinna ograniczyć do minimum wszelką aktywność fizyczną na wolnym powietrzu - szczególnie wymagającą długotrwałego lub wzmożonego wysiłku fizycznego.'
            category_color = 'veryunhealthy'

        elif api['stIndexLevel']['indexLevelName'] == 'Bardzo zły':
            category_description = 'Jakość powietrza jest bardzo zła i ma negatywny wpływ na zdrowie. Osoby chore, starsze, kobiety w ciąży oraz małe dzieci powinny bezwzględnie unikać przebywania na wolnym powietrzu. Pozostała populacja powinna ograniczyć przebywanie na wolnym powietrzu do niezbędnego minimum. Wszelkie aktywności fizyczne na zewnątrz są odradzane. Długotrwała ekspozycja na działanie substancji znajdujących się w powietrzu zwiększa ryzyko wystąpienia zmian m.in. w układzie oddechowym, naczyniowo-sercowym oraz odpornościowym.'
            category_color = 'hazardous'

        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color,})


def about(request):
    return render(request, 'about.html', {})
