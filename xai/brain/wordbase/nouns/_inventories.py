

from xai.brain.wordbase.nouns._inventory import _INVENTORY

#calss header
class _INVENTORIES(_INVENTORY, ):
	def __init__(self,): 
		_INVENTORY.__init__(self)
		self.name = "INVENTORIES"
		self.specie = 'nouns'
		self.basic = "inventory"
		self.jsondata = {}
