
/**
 * [exports description]
 * @author lei on 2019/8/14
 */

import {
    StyleSheet,
} from 'react-native';
import { getFontSizeOfPt, getWidthOfPt } from '../../../utils/utils';

export const Styledemo = StyleSheet.create({
	root: {
		width: getWidthOfPt(375),
		height: getWidthOfPt(667),
		left: getWidthOfPt(0),
		top: getWidthOfPt(0),
	},
	buttonBox: {
		width: getWidthOfPt(161),
		height: getWidthOfPt(66),
		backgroundColor: 'rgb(196, 197, 17)',
		borderWidth: 3,
		borderColor: 'rgb(150, 150, 150)',
		borderRadius: getWidthOfPt(14),
		marginTop: getWidthOfPt(39),
		left: getWidthOfPt(12),
		flexDirection: 'row',
		alignItems: 'center',
	},
	icon3: {
		width: getWidthOfPt(58),
		height: getWidthOfPt(58),
		marginLeft: getWidthOfPt(0),
		top: getWidthOfPt(0),
	},
	icon2: {
		width: getWidthOfPt(58),
		height: getWidthOfPt(58),
		marginLeft: getWidthOfPt(72),
	},
	icon1: {
		width: getWidthOfPt(58),
		height: getWidthOfPt(58),
		marginTop: getWidthOfPt(24),
		left: getWidthOfPt(4),
	},
	ic_launcher: {
		width: getWidthOfPt(30),
		height: getWidthOfPt(30),
		marginLeft: getWidthOfPt(15),
	},
	userName: {
		width: getWidthOfPt(48),
		height: getWidthOfPt(33),
		color: 'rgb(0, 0, 0)',
		fontSize: getFontSizeOfPt(24),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(33),
		marginLeft: getWidthOfPt(24),
	},
	text2: {
		width: getWidthOfPt(96),
		height: getWidthOfPt(66),
		color: 'rgb(0, 0, 0)',
		fontSize: getFontSizeOfPt(24),
		fontFamily: 'PingFangSC-Medium',
		fontWeight: 'bold',
		lineHeight: getWidthOfPt(33),
		marginTop: getWidthOfPt(0),
		left: getWidthOfPt(0),
	},
	text1: {
		width: getWidthOfPt(96),
		height: getWidthOfPt(33),
		color: 'rgb(0, 0, 0)',
		fontSize: getFontSizeOfPt(24),
		fontFamily: 'PingFangSC-Semibold',
		fontWeight: 'bold',
		lineHeight: getWidthOfPt(33),
		marginLeft: getWidthOfPt(104),
		top: getWidthOfPt(0),
	},
	redView: {
		width: getWidthOfPt(156),
		height: getWidthOfPt(69),
		backgroundColor: 'rgb(232, 12, 12)',
		borderWidth: 1,
		borderColor: 'rgb(150, 150, 150)',
		borderRadius: getWidthOfPt(12),
		marginTop: getWidthOfPt(74),
		left: getWidthOfPt(57),
	},
	redText: {
		width: getWidthOfPt(96),
		height: getWidthOfPt(33),
		color: 'rgb(0, 0, 0)',
		fontSize: getFontSizeOfPt(24),
		fontFamily: 'PingFangSC-Regular',
		lineHeight: getWidthOfPt(33),
		left: getWidthOfPt(30),
		top: getWidthOfPt(18),
	},
	id_1: {
		width: getWidthOfPt(258),
		height: getWidthOfPt(58),
		marginTop: getWidthOfPt(58),
		left: getWidthOfPt(35),
		flexDirection: 'row',
	},
	id_2: {
		width: getWidthOfPt(96),
		height: getWidthOfPt(148),
		marginLeft: getWidthOfPt(0),
	},
	id_3: {
		width: getWidthOfPt(226),
		height: getWidthOfPt(148),
		marginTop: getWidthOfPt(113),
		left: getWidthOfPt(77),
		flexDirection: 'row',
		alignItems: 'center',
	},

});
