

#calss header
class _POWERFUL():
	def __init__(self,): 
		self.name = "POWERFUL"
		self.definitions = [u'having a lot of power to control people and events: ', u'having a lot of strength or force: ', u'having a very great effect: ', u'having the power to increase the size of an image of something that is very small or far away many times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
