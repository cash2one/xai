

#calss header
class _FLAMBOYANT():
	def __init__(self,): 
		self.name = "FLAMBOYANT"
		self.definitions = [u'very confident in behaviour, and liking to be noticed by other people, for example because of the way you dress, talk, etc.: ', u'brightly coloured and easily noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
