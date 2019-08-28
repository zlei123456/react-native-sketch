
/**
 * [exports description]
 * @author lei on 2019/8/20
 */

import {
    StyleSheet,
} from 'react-native';
import { getFontSizeOfPt, getWidthOfPt } from '../../../utils/utils';

export const Stylepage1 = StyleSheet.create({
	root: {
		width: getWidthOfPt(335),
		height: getWidthOfPt(110),
		marginTop: getWidthOfPt(-26),
		left: getWidthOfPt(0),
	},
	Group9: {
		width: getWidthOfPt(327),
		height: getWidthOfPt(110),
		backgroundColor: '#f00',
		marginTop: getWidthOfPt(-110),
		left: getWidthOfPt(8),
	},
	Group8: {
		width: getWidthOfPt(90),
		height: getWidthOfPt(110),
		backgroundColor: '#f00',
		marginTop: getWidthOfPt(-110),
		left: getWidthOfPt(0),
	},
	Rectangle: {
		width: getWidthOfPt(90),
		height: getWidthOfPt(30),
		backgroundColor: 'rgb(215, 215, 215)',
		borderWidth: 1,
		borderColor: 'rgb(150, 150, 150)',
		borderRadius: getWidthOfPt(0),
		marginTop: getWidthOfPt(-30),
		left: getWidthOfPt(0),
	},
	time: {
		width: getWidthOfPt(29),
		height: getWidthOfPt(16),
		color: 'rgb(255, 255, 255)',
		fontSize: getFontSizeOfPt(11),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(16),
		marginLeft: getWidthOfPt(0),
		top: getWidthOfPt(4),
	},
	authorName: {
		width: getWidthOfPt(233),
		height: getWidthOfPt(20),
		color: 'rgb(51, 51, 51)',
		fontSize: getFontSizeOfPt(16),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(20),
		marginTop: getWidthOfPt(6),
		left: getWidthOfPt(102),
	},
	storyAbout: {
		width: getWidthOfPt(142),
		height: getWidthOfPt(18),
		color: 'rgb(153, 153, 153)',
		fontSize: getFontSizeOfPt(13),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(18),
		marginTop: getWidthOfPt(4),
		left: getWidthOfPt(102),
	},
	tags: {
		width: getWidthOfPt(201),
		height: getWidthOfPt(18),
		marginTop: getWidthOfPt(32),
		left: getWidthOfPt(102),
	},
	storyName: {
		width: getWidthOfPt(91),
		height: getWidthOfPt(18),
		color: 'rgb(153, 153, 153)',
		fontSize: getFontSizeOfPt(13),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(18),
		marginLeft: getWidthOfPt(6),
		top: getWidthOfPt(0),
	},
	icon_head: {
		width: getWidthOfPt(15),
		height: getWidthOfPt(15),
		marginLeft: getWidthOfPt(65),
		top: getWidthOfPt(2),
	},
	id_1: {
		width: getWidthOfPt(206),
		height: getWidthOfPt(20),
		marginTop: getWidthOfPt(14),
		left: getWidthOfPt(8),
		flexDirection: 'row',
	},
	id_2: {
		width: getWidthOfPt(335),
		height: getWidthOfPt(110),
		left: getWidthOfPt(0),
		top: getWidthOfPt(0),
	},

});
