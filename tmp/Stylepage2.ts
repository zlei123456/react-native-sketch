
/**
 * [exports description]
 * @author lei on 2019/8/30
 */

import {
    StyleSheet,
} from 'react-native';
import { getFontSizeOfPt, getWidthOfPt } from '../../../utils/utils';

export const StylePage2 = StyleSheet.create({
  root: {
    width: getWidthOfPt(335),
    height: getWidthOfPt(82),
    left: getWidthOfPt(0),
    top: getWidthOfPt(0),
  },
  Oval_touch: {
    width: getWidthOfPt(40),
    height: getWidthOfPt(40),
    backgroundColor: 'rgb(215, 215, 215)',
    borderWidth: 1,
    borderColor: 'rgb(150, 150, 150)',
    borderRadius: getWidthOfPt(20.0),
    marginLeft: getWidthOfPt(0),
  },
  icon_addout_linear2: {
    width: getWidthOfPt(40),
    height: getWidthOfPt(40),
    left: getWidthOfPt(0),
    top: getWidthOfPt(0),
  },
  name_touch: {
    includeFontPadding: false,
    width: getWidthOfPt(39),
    height: getWidthOfPt(19),
    color: 'rgb(102, 102, 102)',
    fontSize: getFontSizeOfPt(13),
    lineHeight: getWidthOfPt(18),
    marginTop: getWidthOfPt(0),
    left: getWidthOfPt(0),
  },
  time: {
    includeFontPadding: false,
    width: getWidthOfPt(34),
    height: getWidthOfPt(17),
    color: 'rgb(153, 153, 153)',
    fontSize: getFontSizeOfPt(11),
    lineHeight: getWidthOfPt(16),
    marginTop: getWidthOfPt(0),
    left: getWidthOfPt(0),
  },
  txt: {
    includeFontPadding: false,
    width: getWidthOfPt(289),
    height: getWidthOfPt(43),
    color: 'rgb(51, 51, 51)',
    fontSize: getFontSizeOfPt(15),
    lineHeight: getWidthOfPt(21),
    marginTop: getWidthOfPt(0),
    left: getWidthOfPt(46),
  },
  icon_praise01: {
    width: getWidthOfPt(15),
    height: getWidthOfPt(15),
    marginLeft: getWidthOfPt(6),
  },
  t14: {
    includeFontPadding: false,
    width: getWidthOfPt(15),
    height: getWidthOfPt(16),
    color: 'rgb(153, 153, 153)',
    fontSize: getFontSizeOfPt(13),
    lineHeight: getWidthOfPt(15),
    marginLeft: getWidthOfPt(25),
  },
  richText: {
    includeFontPadding: false,
    width: getWidthOfPt(140),
    marginLeft: getWidthOfPt(49),
  },
  richText_T0: {
    includeFontPadding: false,
    color: 'rgb(98, 163, 228)',
    fontSize: getFontSizeOfPt(14),
    fontWeight: 'normal',
    height: getWidthOfPt(27),
  },
  richText_T1: {
    includeFontPadding: false,
    color: 'rgb(51, 51, 51)',
    fontSize: getFontSizeOfPt(14),
    fontWeight: 'normal',
    height: getWidthOfPt(27),
  },
  id_1: {
    width: getWidthOfPt(39),
    height: getWidthOfPt(34),
    marginLeft: getWidthOfPt(6),
  },
  id_2: {
    width: getWidthOfPt(335),
    height: getWidthOfPt(40),
    marginTop: getWidthOfPt(0),
    left: getWidthOfPt(0),
    flexDirection: 'row',
    alignItems: 'center',
  },

});
