

#calss header
class _MORALISTIC():
	def __init__(self,): 
		self.name = "MORALISTIC"
		self.definitions = [u'judging people and trying to make them behave according to standards of right and wrong that never change and may be too severe or unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
