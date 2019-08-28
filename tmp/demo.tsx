
/**
 * [exports description]
 * @author lei on 2019/8/14
 */
import * as React from 'react';
import { connect } from 'react-redux';
 
import {
    View, TouchableWithoutFeedback,
    Text, TextInput, Image, ImageBackground
} from 'react-native'; 

import { Styledemo } from './Styledemo';

class demo extends React.Component<any, any> {
    render() {
		let ic_launcherValueImg = require('./ic_launcher.png');
		let userNameValueText = '开心';
		let icon3ValueImg = require('./icon_author_fans.png');
		let text1ValueText = '输入文本';
		let text2ValueText = '输入文本
三番四复';
		let icon1ValueImg = require('./icon_author_fans.png');
		let icon2ValueImg = require('./icon_author_fans.png');
		let redTextValueText = '输入文本';

        return (

			<View style={Styledemo.root}
			      key={'root'}
			>
			
				<View style={Styledemo.buttonBox}
				      key={'buttonBox'}
				>
				
					<Image style={Styledemo.ic_launcher}
					          source={ic_launcherValueImg}
					          key={'ic_launcher'}
					>
					
					</Image>
					<Text style={Styledemo.userName}
					      key={'userName'}
					>
						{userNameValueText}
					</Text>
				</View>
				<View style={Styledemo.id_1}
				      key={'id_1'}
				>
				
					<Image style={Styledemo.icon3}
					          source={icon3ValueImg}
					          key={'icon3'}
					>
					
					</Image>
					<Text style={Styledemo.text1}
					      key={'text1'}
					>
						{text1ValueText}
					</Text>
				</View>
				<View style={Styledemo.id_3}
				      key={'id_3'}
				>
				
					<View style={Styledemo.id_2}
					      key={'id_2'}
					>
					
						<Text style={Styledemo.text2}
						      key={'text2'}
						>
							{text2ValueText}
						</Text>
						<Image style={Styledemo.icon1}
						          source={icon1ValueImg}
						          key={'icon1'}
						>
						
						</Image>
					</View>
					<Image style={Styledemo.icon2}
					          source={icon2ValueImg}
					          key={'icon2'}
					>
					
					</Image>
				</View>
				<View style={Styledemo.redView}
				      key={'redView'}
				>
				
					<Text style={Styledemo.redText}
					      key={'redText'}
					>
						{redTextValueText}
					</Text>
				</View>
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

export default connect(mapState, mapDispatch)(demo);
// export default demo
