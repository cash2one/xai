

#calss header
class _BETTER():
	def __init__(self,): 
		self.name = "BETTER"
		self.definitions = [u'in a more suitable, pleasing, or satisfactory way, or to a greater degree: ', u'to a greater degree, when used as the comparative of adjectives beginning with "good" or "well": ', u'used to say that a particular choice would be more satisfactory: ', u'used to give advice or to make a threat: ', u'it would be wiser: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
