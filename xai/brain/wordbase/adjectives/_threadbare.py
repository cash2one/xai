

#calss header
class _THREADBARE():
	def __init__(self,): 
		self.name = "THREADBARE"
		self.definitions = [u'Threadbare material or clothes have become thin or damaged because they have been used a lot: ', u'A threadbare excuse, argument, or idea is not strong and no longer persuades people because it is old or has been used too much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
