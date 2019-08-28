
/**
 * [exports description]
 * @author lei on 2019/8/20
 */
import * as React from 'react';
import { connect } from 'react-redux';
 
import {
    View, TouchableWithoutFeedback,
    Text, TextInput, Image, ImageBackground
} from 'react-native'; 

import { Stylepage1 } from './Stylepage1';

class page1 extends React.Component<any, any> {
    render() {
		let authorNameValueText = '日本漫画家井上日本漫画家井…';
		let storyAboutValueText = '连载中 | 免费 | 1233观看';
		let timeValueText = '4分钟';
		let storyNameValueText = '作者名字叫溜溜';

        return (

			<View style={Stylepage1.id_2}
			      key={'id_2'}
			>
			
				<Text style={Stylepage1.authorName}
				      key={'authorName'}
				>
					{authorNameValueText}
				</Text>
				<View style={Stylepage1.root}
				      key={'root'}
				>
				
					<View style={Stylepage1.tags}
					      key={'tags'}
					>
					
					</View>
					<Text style={Stylepage1.storyAbout}
					      key={'storyAbout'}
					>
						{storyAboutValueText}
					</Text>
					<View style={Stylepage1.id_1}
					      key={'id_1'}
					>
					
						<Text style={Stylepage1.time}
						      key={'time'}
						>
							{timeValueText}
						</Text>
						<View style={Stylepage1.icon_head}
						      key={'icon_head'}
						>
						
						</View>
						<Text style={Stylepage1.storyName}
						      key={'storyName'}
						>
							{storyNameValueText}
						</Text>
					</View>
				</View>
				<View style={Stylepage1.Group9}
				      key={'Group9'}
				>
				
				</View>
				<View style={Stylepage1.Group8}
				      key={'Group8'}
				>
				
				</View>
				<View style={Stylepage1.Rectangle}
				      key={'Rectangle'}
				>
				
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

export default connect(mapState, mapDispatch)(page1);
// export default page1
