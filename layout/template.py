import string
import datetime

template_styleFile = '''
/**
 * [exports description]
 * @author lei on ${date}
 */

import {
    StyleSheet,
} from 'react-native';
${importex}

export const Style${name} = StyleSheet.create({
${style}
});
'''

template_ComponentFile = '''
/**
 * [exports description]
 * @author lei on ${date}
 */
import * as React from 'react';
import { connect } from 'react-redux';
 
import {
    View, TouchableWithoutFeedback,
    Text, TextInput, Image, ImageBackground
} from 'react-native'; 

import { Style${name} } from './Style${name}';

class ${name} extends React.Component<any, any> {
    render() {
${var}
        return (
${render}
        );
    }
}

function mapState(state: any, ownProps: any) {
    return {

    };
}

function mapDispatch(dispatch: any, ownProps: any) {
    return{

    };
}

export default connect(mapState, mapDispatch)(${name});
// export default ${name}
'''

def getStyleFile(name, style, importex):
    print('a')
    conTemp = string.Template(template_styleFile)
    now = datetime.datetime.now()
    nowStr = '{0}/{1}/{2}'.format(now.year, now.month, now.day)
    conTempBuf = conTemp.safe_substitute({
        'name': name,
        'style': style,
        'importex': importex,
        'date': nowStr
    })

    return conTempBuf


def getComponentFile(name, con):
    print('a')
    conTemp = string.Template(template_ComponentFile)
    now = datetime.datetime.now()
    nowStr = '{0}/{1}/{2}'.format(now.year, now.month, now.day)
    render = con['render']
    conTempBuf = conTemp.safe_substitute({
        'name': name,
        'var': con['var'],
        'render': render,
        'date': nowStr
    })

    return conTempBuf

template_View = '''
${space}<View style={Style${name}.${eId}}
${space}      key={'${eId}'}
${space}>
${space}${children}
${space}</View>'''

def getView(eId, name, children, space):
    conTemp = string.Template(template_View)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'children': children,
        'space': space,
    })

    return conTempBuf

template_Button = '''
${space}<TouchableWithoutFeedback key={'${eId}'}
${space}                          onPress={() => {
${space}                          // todo 
${space}                          } }
${space}>
${space}${children}
${space}</TouchableWithoutFeedback>'''

def getButton(eId, children, space):
    conTemp = string.Template(template_Button)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'children': children,
        'space': space,
    })

    return conTempBuf

template_Image = '''
${space}<${cType} style={Style${name}.${eId}}
${space}          source={${src}}
${space}          key={'${eId}'}
${space}>
${space}${children}
${space}</${cType}>'''

def getImage(eId, name, children, cType, src, space):
    conTemp = string.Template(template_Image)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'children': children,
        'cType': cType,
        'src': src,
        'space': space,
    })

    return conTempBuf

template_BaseText = '''
${space}<Text style={Style${name}.${eId}}
${space}      key={'${eId}'}
${space}>
${space}\t${children}
${space}</Text>'''

def getBaseText(eId, name, children, space):
    conTemp = string.Template(template_BaseText)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'children': children,
        'space': space,
    })

    return conTempBuf

template_Text = '''
${space}<Text style={Style${name}.${eId}}
${space}      key={'${eId}'}
${space}>
${space}\t{${text}}
${space}</Text>'''

def getText(eId, name, text, space):
    conTemp = string.Template(template_Text)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'text': text,
        'space': space,
    })

    return conTempBuf

template_TextTouch = '''
${space}<Text style={Style${name}.${eId}}
${space}      key={'${eId}'}
${space}      suppressHighlighting={true}
${space}      onPress={() => {
${space}        // todo
${space}      }}
${space}>
${space}\t{${text}}
${space}</Text>'''

def getTouchText(eId, name, text, space):
    conTemp = string.Template(template_TextTouch)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'text': text,
        'space': space,
    })

    return conTempBuf

template_Input = '''
${space}<TextInput style={Style${name}.${eId}}
${space}           key={'${eId}'}
${space}           keyboardType={'${type}'}
${space}           placeholder={'${placeholder}'}
${space}           underlineColorAndroid={'transparent'}
${space}           onChangeText={ (text) => {
${space}           // todo
 
${space}           }}
${space}/>'''

def getInput(eId, name, type, placeholder, space):
    conTemp = string.Template(template_Input)
    conTempBuf = conTemp.safe_substitute({
        'eId': eId,
        'name': name,
        'space': space,
        'type': type,
        'placeholder': placeholder,
    })

    return conTempBuf