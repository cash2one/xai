

#calss header
class _CONSTANT():
	def __init__(self,): 
		self.name = "CONSTANT"
		self.definitions = [u'happening a lot or all the time: ', u'staying the same, or not getting less or more: ', u'A constant companion or friend who is loyal to you.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
