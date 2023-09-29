import { Config, Connect, ConnectEvents } from '@vkontakte/superappkit';

Config.init({
    appId: 51759872, // идентификатор приложения
});

const oneTapButton = Connect.buttonOneTapAuth({
    // Обязательный параметр в который нужно добавить обработчик событий приходящих из SDK
    callback: function (e) {
        const type = e.type;


        if (!type) {
            return false;
        }


        switch (type) {
            case ConnectEvents.OneTapAuthEventsSDK.LOGIN_SUCCESS: // = 'VKSDKOneTapAuthLoginSuccess'
                console.log(e);
                return false
            // Для этих событий нужно открыть полноценный VK ID чтобы
            // пользователь дорегистрировался или подтвердил телефон
            case ConnectEvents.OneTapAuthEventsSDK.FULL_AUTH_NEEDED: //  = 'VKSDKOneTapAuthFullAuthNeeded'
            case ConnectEvents.OneTapAuthEventsSDK.PHONE_VALIDATION_NEEDED: // = 'VKSDKOneTapAuthPhoneValidationNeeded'
            case ConnectEvents.ButtonOneTapAuthEventsSDK.SHOW_LOGIN: // = 'VKSDKButtonOneTapAuthShowLogin'
                return Connect.redirectAuth({ url: 'https://...', state: 'dj29fnsadjsd82...' }); // url - строка с url, на который будет произведён редирект после авторизации.
            // state - состояние вашего приложение или любая произвольная строка, которая будет добавлена к url после авторизации.
            // Пользователь перешел по кнопке "Войти другим способом"
            case ConnectEvents.ButtonOneTapAuthEventsSDK.SHOW_LOGIN_OPTIONS: // = 'VKSDKButtonOneTapAuthShowLoginOptions'
                // Параметр screen: phone позволяет сразу открыть окно ввода телефона в VK ID
                // Параметр url: ссылка для перехода после авторизации. Должен иметь https схему. Обязательный параметр.
                return Connect.redirectAuth({ screen: 'phone', url: 'https://...' });
        }


        return false;
    },
    // Не обязательный параметр с настройками отображения OneTap
    options: {
        showAlternativeLogin: true, // Отображение кнопки "Войти другим способом"
        displayMode: 'default', // Режим отображения кнопки 'default' | 'name_phone' | 'phone_name'
        buttonStyles: {
            borderRadius: 8, // Радиус скругления кнопок
        }
    },
});


// Получить iframe можно с помощью метода getFrame()
document.body.appendChild(oneTapButton.getFrame());


// Удалить iframe можно с помощью OneTapButton.destroy();