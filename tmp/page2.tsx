
/**
 * [exports description]
 * @author lei on 2019/8/30
 */
import * as React from 'react';
import { connect } from 'react-redux';
 
import {
    View, TouchableWithoutFeedback,
    Text, TextInput, Image, ImageBackground
} from 'react-native'; 

import { StylePage2 } from './StylePage2';

class Page2 extends React.Component<any, any> {
    render() {
    let IconAddoutLinear2Img = require('./icon_addout_linear2.png');
    let NameTouchText = '阿库娅';
    let TimeText = '18天前';
    let RichTextText0 = '坏坏的闻西';
    let RichTextText1 = '：同期待！';
    let T14Text = '14';
    let TxtText = '这个漫画简直不要太好看，完全停不下的节奏，希望接下来能出更多这类好看的作品！';

        return (

        <View style={StylePage2.root}
              key={'root'}
        >
        
          <View style={StylePage2.id_2}
                key={'id_2'}
          >
          
          <TouchableWithoutFeedback key={'Oval_touchT'}
                                    onPress={() => {
                                    // todo 
                                    } }
          >
          
            <View style={StylePage2.Oval_touch}
                  key={'Oval_touch'}
            >
            
            <Image style={StylePage2.icon_addout_linear2}
                      source={IconAddoutLinear2Img}
                      key={'icon_addout_linear2'}
            >
            
            </Image>
            </View>
          </TouchableWithoutFeedback>
            <View style={StylePage2.id_1}
                  key={'id_1'}
            >
            
            <Text style={StylePage2.name_touch}
                  key={'name_touch'}
                  suppressHighlighting={true}
                  onPress={() => {
                    // todo
                  }}
            >
            	{NameTouchText}
            </Text>
            <Text style={StylePage2.time}
                  key={'time'}
            >
            	{TimeText}
            </Text>
            </View>
          <Text style={StylePage2.richText}
                key={'richText'}
          >
          	
          <Text style={StylePage2.richText_T0}
                key={'richText_T0'}
          >
          	{RichTextText0}
          </Text>
          <Text style={StylePage2.richText_T1}
                key={'richText_T1'}
          >
          	{RichTextText1}
          </Text>
          </Text>
          <Text style={StylePage2.t14}
                key={'t14'}
          >
          	{T14Text}
          </Text>
            <View style={StylePage2.icon_praise01}
                  key={'icon_praise01'}
            >
            
            </View>
          </View>
        <Text style={StylePage2.txt}
              key={'txt'}
        >
        	{TxtText}
        </Text>
        </View>
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

export default connect(mapState, mapDispatch)(Page2);
// export default Page2
