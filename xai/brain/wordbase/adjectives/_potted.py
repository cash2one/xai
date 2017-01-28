

#calss header
class _POTTED():
	def __init__(self,): 
		self.name = "POTTED"
		self.definitions = [u'a plant that is grown in a pot', u'used to describe cooked food, especially meat or fish, that is preserved in a closed container: ', u'used to describe a form of a story or book that has been made shorter and simpler and contains only the main facts or features: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
