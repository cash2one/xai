

#calss header
class _BLUE():
	def __init__(self,): 
		self.name = "BLUE"
		self.definitions = [u'of the colour of the sky without clouds on a bright day, or a darker or lighter type of this: ', u'showing or mentioning sexual activity in a way that offends many people: ', u'feeling or showing sadness: ', u'(of meat) cooked so that it is still very red']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
