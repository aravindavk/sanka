port module Converter exposing (..)

import String
import Html exposing (..)
import Html.Attributes
    exposing
        ( class
        , placeholder
        , type_
        , checked
        , readonly
        , value
        , title
        , id
        )
import Browser
import Html.Events
    exposing
        ( onInput
        , onCheck
        , onClick
        )


main =
    Browser.element
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
    , removeExtraSpaces : Bool
    }



-- INIT


init : () -> (Model, Cmd Msg)
init _ =
    ( Model "" "" True False False, Cmd.none )



-- UPDATE


type Msg
    = Check String
    | ConvertedText String
    | EnglishNumbers Bool
    | RemoveExtraSpaces Bool
    | AsciiToUnicode Bool
    | UnicodeToAscii Bool
    | ClearInput


port convert : ( {input: String, a2u: Bool, englishNumbers: Bool, removeExtraSpaces: Bool} ) -> Cmd msg


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Check inputText ->
            ( Model inputText "" model.a2u model.englishNumbers model.removeExtraSpaces
            , convert ( {input=inputText, a2u=model.a2u, englishNumbers=model.englishNumbers, removeExtraSpaces=model.removeExtraSpaces} )
            )

        ConvertedText output ->
            ( { model | outputText = output }, Cmd.none )

        EnglishNumbers value ->
            ( { model | englishNumbers = value }
            , convert ( {input=model.inputText, a2u=model.a2u, englishNumbers=value, removeExtraSpaces=model.removeExtraSpaces} )
            )

        RemoveExtraSpaces value ->
            ( { model | removeExtraSpaces = value }
            , convert ( {input=model.inputText, a2u=model.a2u, englishNumbers=model.englishNumbers, removeExtraSpaces=value} )
            )

        AsciiToUnicode value ->
            ( { model | a2u = value }
            , convert ( {input=model.inputText, a2u=value, englishNumbers=model.englishNumbers, removeExtraSpaces=model.removeExtraSpaces} )
            )

        UnicodeToAscii value ->
            ( { model | a2u = (value == False) }
            , convert ( {input=model.inputText, a2u=(value == False), englishNumbers=model.englishNumbers, removeExtraSpaces=model.removeExtraSpaces} )
            )

        ClearInput ->
            ( Model "" "" True False False, Cmd.none )



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
        div [ id "app" ]
        [
        div [ class "container" ]
            [ div [ class "controls" ]
                [ div [ class "english-numbers" ]
                    [ label []
                        [ input
                            [ type_ "checkbox"
                            , checked model.englishNumbers
                            , onCheck EnglishNumbers
                            ]
                            []
                        , text "ಆಂಗ್ಲ ಸಂಖ್ಯೆಗಳು"
                        ],
                      label []
                        [ input
                            [ type_ "checkbox"
                            , checked model.removeExtraSpaces
                            , onCheck RemoveExtraSpaces
                            ]
                            []
                        , text "ಹೆಚ್ಚಿನ Space ತೆಗೆಯಿರಿ"
                        ]
                    ]
                , div [ class "convert-type" ]
                    [ label []
                        [ input
                            [ type_ "radio"
                            , checked (model.a2u == True)
                            , onCheck AsciiToUnicode
                            ]
                            []
                        , text "ASCII to Unicode"
                        ]
                    , label []
                        [ input
                            [ type_ "radio"
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
                    , title ((String.fromInt num_words) ++ " ಪದ(ಗಳು)")
                    ]
                    [ text ((String.fromInt num_words))
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
            ]



-- SUBSCRIPTIONS


port converted_text : (String -> msg) -> Sub msg


subscriptions : Model -> Sub Msg
subscriptions model =
    converted_text ConvertedText
