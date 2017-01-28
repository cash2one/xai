

#calss header
class _MERCIFUL():
	def __init__(self,): 
		self.name = "MERCIFUL"
		self.definitions = [u'someone who is merciful is willing to be kind to and forgive people who are in their power: ', u'used to say that you are grateful for an event or situation because it stops something unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
