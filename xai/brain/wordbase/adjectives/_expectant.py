

#calss header
class _EXPECTANT():
	def __init__(self,): 
		self.name = "EXPECTANT"
		self.definitions = [u'thinking that something pleasant or exciting is going to happen: ', u'used to refer to a woman who is pregnant or a man whose partner is pregnant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
