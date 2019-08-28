
/**
 * [exports description]
 * @author lei on 2019/8/28
 */
import * as React from 'react';
import { connect } from 'react-redux';
 
import {
    View, TouchableWithoutFeedback,
    Text, TextInput, Image, ImageBackground
} from 'react-native'; 

import { Stylepage3 } from './Stylepage3';

class page3 extends React.Component<any, any> {
    render() {
    let 布拉格广场ValueText = '布拉格广场';
    let 10天前ValueText = '10天前';
    let 14ValueText = '14';
    let 期待后续的更新！ValueText = '期待后续的更新！';
    let 坏坏的闻西：同期待！ValueText = '坏坏的闻西：同期待！';
    let 人间蒸发：不知道后面的发展怎样，应该有不ValueText = '人间蒸发：不知道后面的发展怎样，应该有不错的走向。';
    let 布拉格回复小迷你：你说的好棒啊！ValueText = '布拉格回复小迷你：你说的好棒啊！';
    let 共8条回复>ValueText = '共8条回复>';

        return (

      <View style={Stylepage3.id_2}
            key={'id_2'}
      >
      
        <View style={Stylepage3.OvalCopy}
              key={'OvalCopy'}
        >
        
        </View>
        <View style={Stylepage3.id_1}
              key={'id_1'}
        >
        
          <Text style={Stylepage3.布拉格广场}
                key={'布拉格广场'}
          >
          	{布拉格广场ValueText}
          </Text>
          <Text style={Stylepage3.10天前}
                key={'10天前'}
          >
          	{10天前ValueText}
          </Text>
        </View>
        <Text style={Stylepage3.14}
              key={'14'}
        >
        	{14ValueText}
        </Text>
        <View style={Stylepage3.icon_praise02}
              key={'icon_praise02'}
        >
        
        </View>
      </View>
      <Text style={Stylepage3.期待后续的更新！}
            key={'期待后续的更新！'}
      >
      	{期待后续的更新！ValueText}
      </Text>
      <View style={Stylepage3.Rectangle}
            key={'Rectangle'}
      >
      
        <Text style={Stylepage3.坏坏的闻西：同期待！}
              key={'坏坏的闻西：同期待！'}
        >
        	{坏坏的闻西：同期待！ValueText}
        </Text>
        <Text style={Stylepage3.人间蒸发：不知道后面的发展怎样，应该有不}
              key={'人间蒸发：不知道后面的发展怎样，应该有不'}
        >
        	{人间蒸发：不知道后面的发展怎样，应该有不ValueText}
        </Text>
        <Text style={Stylepage3.布拉格回复小迷你：你说的好棒啊！}
              key={'布拉格回复小迷你：你说的好棒啊！'}
        >
        	{布拉格回复小迷你：你说的好棒啊！ValueText}
        </Text>
        <Text style={Stylepage3.共8条回复>}
              key={'共8条回复>'}
        >
        	{共8条回复>ValueText}
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

export default connect(mapState, mapDispatch)(page3);
// export default page3
