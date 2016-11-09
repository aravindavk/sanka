port module Converter exposing (..)

import String
import Html exposing (..)
import Html.Attributes
    exposing
        ( class
        , placeholder
        , type'
        , checked
        , readonly
        , value
        , title
        )
import Html.App as Html
import Html.Events
    exposing
        ( onInput
        , onCheck
        , onClick
        )


main =
    Html.program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }



-- MODEL


type alias Model =
    { inputText : String
    , outputText : String
    , a2u : Bool
    , englishNumbers : Bool
    }



-- INIT


init : ( Model, Cmd Msg )
init =
    ( Model "" "" True False, Cmd.none )



-- UPDATE


type Msg
    = Check String
    | ConvertedText String
    | EnglishNumbers Bool
    | AsciiToUnicode Bool
    | UnicodeToAscii Bool
    | ClearInput


port convert : ( String, Bool, Bool ) -> Cmd msg


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Check inputText ->
            ( Model inputText "" model.a2u model.englishNumbers
            , convert ( inputText, model.a2u, model.englishNumbers )
            )

        ConvertedText output ->
            ( { model | outputText = output }, Cmd.none )

        EnglishNumbers value ->
            ( { model | englishNumbers = value }
            , convert ( model.inputText, model.a2u, value )
            )

        AsciiToUnicode value ->
            ( { model | a2u = value }
            , convert ( model.inputText, value, model.englishNumbers )
            )

        UnicodeToAscii value ->
            ( { model | a2u = (value == False) }
            , convert ( model.inputText, (value == False), model.englishNumbers )
            )

        ClearInput ->
            ( Model "" "" True False, Cmd.none )



-- VIEW


placeholderTextLeft : Bool -> String
placeholderTextLeft a2u =
    (if a2u then
        "ಬರಹ/ನುಡಿಯಿಂದ ಯುನಿಕೋಡ್ ಗೆ"
     else
        "ಯುನಿಕೋಡ್ ನಿಂದ ಬರಹ/ನುಡಿಗೆ"
    )
        ++ " ಬದಲಾಯಿಸಲು ಇಲ್ಲಿ ಬರೆಯಿರಿ..."


placeholderTextRight : Bool -> String
placeholderTextRight a2u =
    (if a2u then
        "ಬರಹ/ನುಡಿಯಿಂದ ಯುನಿಕೋಡ್ ಗೆ"
     else
        "ಯುನಿಕೋಡ್ ನಿಂದ ಬರಹ/ನುಡಿಗೆ"
    )
        ++ " ಬದಲಾವಣೆಗೊಂಡ ಪಠ್ಯ.."


view : Model -> Html Msg
view model =
    let
        num_words =
            if model.inputText == "" then
                0
            else
                (List.length (String.words model.inputText))
    in
        div [ class "container" ]
            [ div [ class "controls" ]
                [ div [ class "english-numbers" ]
                    [ label []
                        [ input
                            [ type' "checkbox"
                            , checked model.englishNumbers
                            , onCheck EnglishNumbers
                            ]
                            []
                        , text "ಆಂಗ್ಲ ಸಂಖ್ಯೆಗಳು"
                        ]
                    ]
                , div [ class "convert-type" ]
                    [ label []
                        [ input
                            [ type' "radio"
                            , checked (model.a2u == True)
                            , onCheck AsciiToUnicode
                            ]
                            []
                        , text "ASCII to Unicode"
                        ]
                    , label []
                        [ input
                            [ type' "radio"
                            , checked (model.a2u == False)
                            , onCheck UnicodeToAscii
                            ]
                            []
                        , text "Unicode to ASCII"
                        ]
                    ]
                , button [ onClick ClearInput ] [ text "Reset" ]
                ]
            , div [ class "clear" ] []
            , div [ class "left" ]
                [ span
                    [ class "num-words"
                    , title ((toString num_words) ++ " ಪದ(ಗಳು)")
                    ]
                    [ text ((toString num_words))
                    ]
                , text (placeholderTextLeft model.a2u)
                , textarea
                    [ onInput Check
                    , value model.inputText
                    ]
                    []
                ]
            , div [ class "right" ]
                [ text (placeholderTextRight model.a2u)
                , textarea [ readonly True ] [ text model.outputText ]
                ]
            , div [ class "clear" ] []
            ]



-- SUBSCRIPTIONS


port converted_text : (String -> msg) -> Sub msg


subscriptions : Model -> Sub Msg
subscriptions model =
    converted_text ConvertedText
