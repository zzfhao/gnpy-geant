# coding=utf-8
""" link_description.py contains the full description of that OLE has to emulate.
    It contains a list of dictionaries, following the structure of the link and each element of the list describes one
    component.

    'comp_cat': the kind of link component:
        PC: a passive component defined by a loss at a certain frequency and a loss tilt
        OA: an optical amplifier defined by a gain at a certain frequency, a gain tilt and a noise figure
        fiber: a span of fiber described by the type and the length
    'comp_id': is an id identifying the component. It has to be unique for each component!

    extra fields for PC:
        'ref_freq': the frequency at which the 'loss' parameter is evaluated [THz]
        'loss': the loss at the frequency 'ref_freq' [dB]
        'loss_tlt': the frequency dependent loss [dB/THz]
    extra fields for OA:
        'ref_freq': the frequency at which the 'gain' parameter is evaluated [THz]
        'gain': the gain at the frequency 'ref_freq' [dB]
        'gain_tlt': the frequency dependent gain [dB/THz]
        'noise_figure': 5he noise figure of the optical amplifier [dB]
    extra fields for fiber:
        'fiber_type': a string calling the type of fiber described in the file fiber_parameters.py
        'length': the fiber length [km]

"""
"""
smf = {
    'comp_cat': 'fiber',
    'comp_id': '',
    'fiber_type': 'SMF',
    'length': 100
    }

oa = {
    'comp_cat': 'OA',
    'comp_id': '',
    'ref_freq': 193.5,
    'gain': 20,
    'gain_tlt': 0.0,
    'noise_figure': 5
    }

pc = {
    'comp_cat': 'PC',
    'comp_id': '04',
    'ref_freq': 193.,
    'loss': 2.0,
    'loss_tlt': 0.0
    }

link = []
# interleaved arrange of fiber and oa, id from 0 to 39
for index in range(30):
    smf['comp_id'] = '%03d' % (2 * index)
    oa['comp_id'] = '%03d' % (2 * index + 1)
    link += [dict(smf)]
    link += [dict(oa)]
# put one pc at the end, id = 40
pc['comp_id'] = '%03d' % 60
link += [dict(pc)]
"""
#wien to prag
link = [
        # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '00',
         'ref_freq': 193.5,
         'gain': 17,
         'gain_tlt': 0,
         'noise_figure': 6
        },

        # SPAN 1
            #G.652
        {
    	'comp_cat': 'fiber',
   	    'comp_id': '01',
    	'fiber_type': 'SMF0',
    	'length': 21.6
    	},
            #G.655
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'NZDF0',
        'length': 86.4
        },

        # GAIN 2    
    	{
    	 'comp_cat': 'OA',
    	 'comp_id': '02',
    	 'ref_freq': 193.5,
    	 'gain': 20,
    	 'gain_tlt': 0,
    	 'noise_figure': 4.8
    	},

        # SPAN 2
	    {
    	'comp_cat': 'fiber',
    	'comp_id': '03',
    	'fiber_type': 'NZDF1',
    	'length': 78.8
    	},

        # GAIN 3
	    {
    	'comp_cat': 'OA',
    	'comp_id': '04',
    	'ref_freq': 193.5,
    	'gain': 20,
    	'gain_tlt': 0,
    	'noise_figure': 4.8
    	},

        # SPAN 3            

            #G.655
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'NZDF2',
        'length': 87.75
        },  
            #G.652
	    {
    	'comp_cat': 'fiber',
       	'comp_id': '05',
       	'fiber_type': 'SMF2',
       	'length': 9.75
    	},
    

        # GAIN 4
	    {
   	    'comp_cat': 'OA',
    	'comp_id': '07',
    	'ref_freq': 193.5,
    	'gain': 10,
    	'gain_tlt': 0,
    	'noise_figure': 4.8
    	},

        # SPAN 4
	    {
      	'comp_cat': 'fiber',
       	'comp_id': '08',
       	'fiber_type': 'SMF3',
       	'length': 5.6
    	},

        # GAIN 5
	    {
    	 'comp_cat': 'OA',
    	 'comp_id': '09',
    	 'ref_freq': 193.5,
    	 'gain': 20,
    	 'gain_tlt': 0,
    	 'noise_figure': 4.8
	    },

        # SPAN 5
	    {
    	'comp_cat': 'fiber',
       	'comp_id': '10',
       	'fiber_type': 'SMF4',
       	'length': 118
    	},

        # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '11',
         'ref_freq': 193.5,
         'gain': 20,
         'gain_tlt': 0,
         'noise_figure': 4.8
        },

        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '12',
        'fiber_type': 'SMF5',
        'length': 109
        }
]
print (link)
"""
link = [            #310km
       # SPAN 1
        {
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 28.7
        },
       # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 7.175,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 2
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'SMF1',
        'length': 52.7
        },
       # GAIN 2
        {
         'comp_cat': 'OA',
         'comp_id': '2',
         'ref_freq': 193.5,
         'gain': 13.175,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 3
        {
        'comp_cat': 'fiber',
        'comp_id': '03',
        'fiber_type': 'SMF1',
        'length': 40.7
        },
       # GAIN 3
        {
         'comp_cat': 'OA',
         'comp_id': '3',
         'ref_freq': 193.5,
         'gain': 10.175,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 4
        {
        'comp_cat': 'fiber',
        'comp_id': '04',
        'fiber_type': 'SMF1',
        'length': 38.3
        },
       # GAIN 4
        {
         'comp_cat': 'OA',
         'comp_id': '4',
         'ref_freq': 193.5,
         'gain': 9.575,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 5
        {
        'comp_cat': 'fiber',
        'comp_id': '05',
        'fiber_type': 'SMF1',
        'length': 103.3
        },
       # GAIN 5
        {
         'comp_cat': 'OA',
         'comp_id': '5',
         'ref_freq': 193.5,
         'gain': 25.825,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 47.1
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 11.775,
         'gain_tlt': 0,
         'noise_figure': 5
        }
]
"""
"""
def setlength (position, value):
    link[position]["length"] = value
    return
def setgain (position, value):
    link[position]["gain"] = value
    return
#1077km
n = 0
link = []


while n <= 11:
    if n%2==0:
        link.append({
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 28.7
        })
        n=n+1
    else:
        link.append({
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 7.175,
         'gain_tlt': 0,
         'noise_figure': 5
        })
        n=n+1
print(link) 

def setlength (position, value):
    link[position]["length"] = value
    return
def setgain (position, value):
    link[position]["gain"] = value
    return
    """
"""
link = [            #1077km
       # SPAN 1
        {
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 50.5
        },
       # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 12.625,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 2
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'SMF1',
        'length': 102
        },
       # GAIN 2
        {
         'comp_cat': 'OA',
         'comp_id': '2',
         'ref_freq': 193.5,
         'gain': 25.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 3
        {
        'comp_cat': 'fiber',
        'comp_id': '03',
        'fiber_type': 'SMF1',
        'length': 84.6
        },
       # GAIN 3
        {
         'comp_cat': 'OA',
         'comp_id': '3',
         'ref_freq': 193.5,
         'gain': 21.15,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 4
        {
        'comp_cat': 'fiber',
        'comp_id': '04',
        'fiber_type': 'SMF1',
        'length': 67.6
        },
       # GAIN 4
        {
         'comp_cat': 'OA',
         'comp_id': '4',
         'ref_freq': 193.5,
         'gain': 16.9,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 5
        {
        'comp_cat': 'fiber',
        'comp_id': '05',
        'fiber_type': 'SMF1',
        'length': 38
        },
       # GAIN 5
        {
         'comp_cat': 'OA',
         'comp_id': '5',
         'ref_freq': 193.5,
         'gain': 9.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '07',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        }
]
setlength(12,70.7);
setlength(14,66.6);
setlength(16,75.3);
setlength(18,30);
setlength(20,95.1);
setlength(22,36.4);
setlength(24,62.4);
setlength(26,49.9);
setlength(28,38.3);
setlength(30,103.3);
setlength(32,47.1);
setgain(13,17.675);
setgain(15,16.65);
setgain(17,18.825);
setgain(19,7.5);
setgain(21,23.775);
setgain(23,9.1);
setgain(25,15.6);
setgain(27,12.475);
setgain(29,9.575);
setgain(31,25.825);
setgain(33,11.775);
"""
"""
link = [            #1419km
       # SPAN 1
        {
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 50.5
        },
       # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 12.625,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 2
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'SMF1',
        'length': 102
        },
       # GAIN 2
        {
         'comp_cat': 'OA',
         'comp_id': '2',
         'ref_freq': 193.5,
         'gain': 25.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 3
        {
        'comp_cat': 'fiber',
        'comp_id': '03',
        'fiber_type': 'SMF1',
        'length': 84.6
        },
       # GAIN 3
        {
         'comp_cat': 'OA',
         'comp_id': '3',
         'ref_freq': 193.5,
         'gain': 21.15,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 4
        {
        'comp_cat': 'fiber',
        'comp_id': '04',
        'fiber_type': 'SMF1',
        'length': 67.6
        },
       # GAIN 4
        {
         'comp_cat': 'OA',
         'comp_id': '4',
         'ref_freq': 193.5,
         'gain': 16.9,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 5
        {
        'comp_cat': 'fiber',
        'comp_id': '05',
        'fiber_type': 'SMF1',
        'length': 38
        },
       # GAIN 5
        {
         'comp_cat': 'OA',
         'comp_id': '5',
         'ref_freq': 193.5,
         'gain': 9.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '07',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        }
]
setlength(0,50.5);
setlength(2,102);
setlength(4,84.6);
setlength(6,67.6);
setlength(8,38);
setlength(10,59.4);
setlength(12,70.7);
setlength(14,66.6);
setlength(16,55.6);
setlength(18,93.1);
setlength(20,93.1);
setlength(22,59.6);
setlength(24,49.9);
setlength(26,49.4);
setlength(28,55.9);
setlength(30,55.4);
setlength(32,66.8);
setlength(34,62.4);
setlength(36,49.9);
setlength(38,38.3);
setlength(40,103.3);
setlength(42,47.1);
setgain(1,12.625);
setgain(3,25.5);
setgain(5,21.15);
setgain(7,16.9);
setgain(9,9.5);
setgain(11,14.85);
setgain(13,17.675);
setgain(15,16.65);
setgain(17,13.9);
setgain(19,23.275);
setgain(21,23.275);
setgain(23,14.9);
setgain(25,12.475);
setgain(27,12.35);
setgain(29,13.975);
setgain(31,13.85);
setgain(33,16.7);
setgain(35,15.6);
setgain(37,12.475);
setgain(39,9.575);
setgain(41,25.825);
setgain(43,11.775);
"""
"""
link = [            #1723km
       # SPAN 1
        {
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 50.5
        },
       # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 12.625,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 2
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'SMF1',
        'length': 102
        },
       # GAIN 2
        {
         'comp_cat': 'OA',
         'comp_id': '2',
         'ref_freq': 193.5,
         'gain': 25.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 3
        {
        'comp_cat': 'fiber',
        'comp_id': '03',
        'fiber_type': 'SMF1',
        'length': 84.6
        },
       # GAIN 3
        {
         'comp_cat': 'OA',
         'comp_id': '3',
         'ref_freq': 193.5,
         'gain': 21.15,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 4
        {
        'comp_cat': 'fiber',
        'comp_id': '04',
        'fiber_type': 'SMF1',
        'length': 67.6
        },
       # GAIN 4
        {
         'comp_cat': 'OA',
         'comp_id': '4',
         'ref_freq': 193.5,
         'gain': 16.9,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 5
        {
        'comp_cat': 'fiber',
        'comp_id': '05',
        'fiber_type': 'SMF1',
        'length': 38
        },
       # GAIN 5
        {
         'comp_cat': 'OA',
         'comp_id': '5',
         'ref_freq': 193.5,
         'gain': 9.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '07',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        }
]
setlength(0,29.5);
setlength(2,45.5);
setlength(4,49.6);
setlength(6,75.5);
setlength(8,47);
setlength(10,34);
setlength(12,54.9);
setlength(14,50.1);
setlength(16,71.7);
setlength(18,24.5);
setlength(20,42.4);
setlength(22,74.6);
setlength(24,47.4);
setlength(26,35.4);
setlength(28,63.8);
setlength(30,53.4);
setlength(32,83.4);
setlength(34,76.1);
setlength(36,69.8);
setlength(38,53.7);
setlength(40,39.6);
setlength(42,100.4);
setlength(44,26.6);
setlength(46,63.5);
setlength(48,41.1);
setlength(50,68.8);
setlength(52,62.4);
setlength(54,49.9);
setlength(56,38.3);
setlength(58,103.3);
setlength(60,47);

setgain(1,7.375);
setgain(3,11.375);
setgain(5,12.4);
setgain(7,18.875);
setgain(9,11.75);
setgain(11,8.5);
setgain(13,13.725);
setgain(15,12.525);
setgain(17,17.925);
setgain(19,6.125);
setgain(21,10.6);
setgain(23,18.65);
setgain(25,11.85);
setgain(27,8.85);
setgain(29,15.95);
setgain(31,13.35);
setgain(33,20.85);
setgain(35,19.025);
setgain(37,17.45);
setgain(39,13.425);
setgain(41,9.9);
setgain(43,25.1);
setgain(45,6.65);
setgain(47,15.875);
setgain(49,10.275);
setgain(51,17.2);
setgain(53,15.6);
setgain(55,12.475);
setgain(57,9.575);
setgain(59,25.825);
setgain(61,11.75);
"""
"""
link = [            #2238km
       # SPAN 1
        {
        'comp_cat': 'fiber',
        'comp_id': '01',
        'fiber_type': 'SMF1',
        'length': 50.5
        },
       # GAIN 1
        {
         'comp_cat': 'OA',
         'comp_id': '1',
         'ref_freq': 193.5,
         'gain': 12.625,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 2
        {
        'comp_cat': 'fiber',
        'comp_id': '02',
        'fiber_type': 'SMF1',
        'length': 102
        },
       # GAIN 2
        {
         'comp_cat': 'OA',
         'comp_id': '2',
         'ref_freq': 193.5,
         'gain': 25.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 3
        {
        'comp_cat': 'fiber',
        'comp_id': '03',
        'fiber_type': 'SMF1',
        'length': 84.6
        },
       # GAIN 3
        {
         'comp_cat': 'OA',
         'comp_id': '3',
         'ref_freq': 193.5,
         'gain': 21.15,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 4
        {
        'comp_cat': 'fiber',
        'comp_id': '04',
        'fiber_type': 'SMF1',
        'length': 67.6
        },
       # GAIN 4
        {
         'comp_cat': 'OA',
         'comp_id': '4',
         'ref_freq': 193.5,
         'gain': 16.9,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 5
        {
        'comp_cat': 'fiber',
        'comp_id': '05',
        'fiber_type': 'SMF1',
        'length': 38
        },
       # GAIN 5
        {
         'comp_cat': 'OA',
         'comp_id': '5',
         'ref_freq': 193.5,
         'gain': 9.5,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '07',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        },
        # SPAN 6
        {
        'comp_cat': 'fiber',
        'comp_id': '06',
        'fiber_type': 'SMF1',
        'length': 59.4
        },
       # GAIN 6
        {
         'comp_cat': 'OA',
         'comp_id': '6',
         'ref_freq': 193.5,
         'gain': 14.85,
         'gain_tlt': 0,
         'noise_figure': 5
        }
]
setlength(0,50.5);
setlength(2,102);
setlength(4,84.6);
setlength(6,67.6);
setlength(8,38);
setlength(10,59.4);
setlength(12,70.7);
setlength(14,73.2);
setlength(16,50.8);
setlength(18,24.7);
setlength(20,77.3);
setlength(22,42);
setlength(24,91.5);
setlength(26,45);
setlength(28,74.2);
setlength(30,68);
setlength(32,73.9);
setlength(34,105);
setlength(36,20);
setlength(38,70);
setlength(40,70);
setlength(42,25.2);
setlength(44,76.2);
setlength(46,58.6);
setlength(48,33.6);
setlength(50,93.1);
setlength(52,55.6);
setlength(54,75.3);
setlength(56,30);
setlength(58,95.1);
setlength(60,36.4);
setlength(62,62.4);
setlength(64,49.9);
setlength(66,38.3);
setlength(68,103.3);
setlength(70,47.1);

setgain(1,12.625);
setgain(3,25.5);
setgain(5,21.15);
setgain(7,16.9);
setgain(9,9.5);
setgain(11,14.85);
setgain(13,17.675);
setgain(15,18.3);
setgain(17,12.7);
setgain(19,6.175);
setgain(21,19.325);
setgain(23,10.5);
setgain(25,22.875);
setgain(27,11.25);
setgain(29,18.55);
setgain(31,17);
setgain(33,18.475);
setgain(35,26.25);
setgain(37,5);
setgain(39,17.5);
setgain(41,17.5);
setgain(43,6.3);
setgain(45,19.05);
setgain(47,14.65);
setgain(49,8.4);
setgain(51,23.275);
setgain(53,13.9);
setgain(55,18.825);
setgain(57,7.5);
setgain(59,23.775);
setgain(61,9.1);
setgain(63,15.6);
setgain(65,12.475);
setgain(67,9.575);
setgain(69,25.825);
setgain(71,11.775);
"""
"""for x in link:
    if link.index(x) % 2 != 0:
        print(x['gain'])
for x in link:
    if link.index(x) % 2 == 0:
        print(x['length'])"""