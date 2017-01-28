

#calss header
class _RID():
	def __init__(self,): 
		self.name = "RID"
		self.definitions = [u'to not now have an unwanted or unpleasant task, object, or person: ', u'to remove or throw away something unwanted: ', u'to sell an old or unwanted possession: ', u'to send away someone annoying or to persuade them to leave: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
