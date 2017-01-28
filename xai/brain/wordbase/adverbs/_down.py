

#calss header
class _DOWN():
	def __init__(self,): 
		self.name = "DOWN"
		self.definitions = [u'in or towards a low or lower position, from a higher one: ', u'moving from above and onto a surface: ', u'firmly in place or into position: ', u'in or towards a lower level, a smaller amount, or a simpler state: ', u'If you burn, cut, or knock something or someone down, you cause it, him, or her to fall to the ground, usually damaged, destroyed, or injured: ', u'in writing or on paper: ', u'used, especially with prepositions, to emphasize that a place is at some distance from you or from somewhere considered to be central: ', u'in or towards the south: ', u'from an older person to a younger one: ', u'inside your stomach: ', u'at the time of buying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
